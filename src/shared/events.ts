/**
 * Standardized Event Types for the OVERLORD Pipeline
 */

export enum PipelineEvent {
  VIDEO_UPLOADED = 'video.uploaded',
  TRANSCRIPTION_COMPLETED = 'transcription.completed',
  CLIPS_IDENTIFIED = 'clips.identified',
  VIDEO_RENDER_COMPLETED = 'video.render.completed',
  PIPELINE_FAILED = 'pipeline.failed'
}

export interface VideoUploadedPayload {
  videoId: string;
  s3Key: string;
  userId: string;
  originalName: string;
}

export interface ClipSegment {
  startTime: number;
  endTime: number;
  reason: string; // Why AI chose this
  title: string;
}

export interface ClipsIdentifiedPayload {
  videoId: string;
  segments: ClipSegment[];
}