import { Queue } from 'bullmq';
import { PipelineEvent, VideoUploadedPayload } from '../shared/events';

const videoQueue = new Queue('video-pipeline', {
  connection: { host: 'redis', port: 6379 }
});

export class IngestionService {
  /**
   * Called after a successful S3 upload
   */
  async handleNewUpload(data: { videoId: string; s3Key: string; userId: string; filename: string }) {
    console.log(`[Ingestion] Processing new upload: ${data.videoId}`);
    
    const payload: VideoUploadedPayload = {
      videoId: data.videoId,
      s3Key: data.s3Key,
      userId: data.userId,
      originalName: data.filename
    };

    // Add to BullMQ for the Transcription Worker to pick up
    await videoQueue.add(PipelineEvent.VIDEO_UPLOADED, payload, {
      attempts: 3,
      backoff: { type: 'exponential', delay: 5000 }
    });

    return { status: 'queued', videoId: data.videoId };
  }
}