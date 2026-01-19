# OVERLORD: Event-Driven System Architecture

## 1. High-Level Overview
The system is designed as a distributed, event-driven pipeline to handle compute-intensive video processing tasks. By decoupling ingestion from processing, we ensure high availability and the ability to scale worker nodes independently based on queue depth.

## 2. Infrastructure Components
- **API Gateway:** Entry point for clients (Web/Mobile).
- **Ingestion Service:** Handles file uploads and initial metadata validation.
- **Object Storage (S3):** Stores raw long-form videos and processed short clips.
- **Message Broker (Redis/BullMQ):** Manages the "Video Pipeline" event bus.
- **Worker Cluster:**
    - **Transcription Worker:** Uses Whisper/Deepgram to extract text and timestamps.
    - **AI Analysis Worker:** Uses GPT-4o/Claude to identify "Viral Hooks" and speaker segments.
    - **Video Processing Worker:** Uses FFmpeg and OpenCV for 9:16 cropping and caption burning.
- **Database (PostgreSQL):** Stores video metadata, clip coordinates, and user data.
- **Cache (Redis):** Real-time job status tracking for the UI.

## 3. Data Flow (The Pipeline)
1. **Upload:** User uploads long-form video -> S3.
2. **Trigger:** Ingestion service emits `VIDEO_UPLOADED` event.
3. **Transcribe:** Transcription worker picks up job -> Generates JSON transcript -> Emits `TRANSCRIPTION_COMPLETED`.
4. **Analyze:** AI Worker analyzes transcript + visual cues -> Identifies timestamps for clips -> Emits `CLIPS_IDENTIFIED`.
5. **Render:** Rendering workers process FFmpeg commands (Crop, Resize, Subtitle) -> Uploads to S3 -> Emits `PROCESSING_FINISHED`.
6. **Notify:** Webhook/Push notification sends the "Ready" status to the user.