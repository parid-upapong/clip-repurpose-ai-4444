# Computer Vision Strategy: Smart Reframing

## Overview
To transform horizontal content (16:9) into vertical (9:16) for TikTok/Reels, our CV pipeline implements **Active Speaker Tracking**. Unlike static center-cropping, this ensures the most relevant subject is always in frame.

## Implementation Details
1. **Detection Layer**: We use MediaPipe Face Mesh for high-speed tracking (60+ FPS on CPU). We extract 468 3D landmarks to monitor facial presence.
2. **Active Speaker Identification**: 
   - We calculate the "Lip Distance" (Euclidean distance between landmarks 13 and 14).
   - The subject with the highest variance/distance in lip movement over a 5-frame window is flagged as the active speaker.
3. **Smooth Motion (Cinematic LERP)**:
   - To avoid "jittery" camera movements when a speaker moves, we use Linear Interpolation (LERP) for the crop window's X-coordinate.
   - `New_X = (Old_X * 0.9) + (Target_X * 0.1)`
4. **Contextual Fallback**:
   - If no faces are detected, the system defaults to a **Saliency Map** (finding high-contrast or moving objects) or falls back to center-crop.

## Scaling
The `VideoProcessor` is designed to be wrapped in a Celery/BullMQ worker, utilizing GPU acceleration (via `cv2.cuda`) when available in production environments.