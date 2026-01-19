export type JobStatus = 'pending' | 'processing' | 'completed' | 'failed';

export interface VideoClip {
  id: string;
  startTime: number;
  endTime: number;
  viralityScore: number;
  title: string;
  transcript: string;
  status: JobStatus;
  previewUrl: string;
}

export interface VideoProject {
  id: string;
  originalTitle: string;
  originalUrl: string;
  duration: number;
  clips: VideoClip[];
  createdAt: string;
}