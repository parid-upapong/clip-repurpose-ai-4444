import { Worker, Job } from 'bullmq';
import ffmpeg from 'fluent-ffmpeg';
import { PipelineEvent, ClipsIdentifiedPayload } from '../shared/events';

/**
 * Worker responsible for cropping 16:9 to 9:16 and burning subtitles
 */
const worker = new Worker('video-pipeline', async (job: Job) => {
  if (job.name === PipelineEvent.CLIPS_IDENTIFIED) {
    const { videoId, segments } = job.data as ClipsIdentifiedPayload;

    console.log(`[Editor] Starting render for ${segments.length} clips from video ${videoId}`);

    for (const segment of segments) {
      await processClip(videoId, segment);
    }
  }
}, { connection: { host: 'redis', port: 6379 } });

async function processClip(videoId: string, segment: any) {
  return new Promise((resolve, reject) => {
    ffmpeg(`/tmp/${videoId}_raw.mp4`)
      .setStartTime(segment.startTime)
      .setDuration(segment.endTime - segment.startTime)
      // Intelligent Crop: Center crop to 9:16 (1080x1920)
      .videoFilters([
        'crop=in_h*9/16:in_h',
        'scale=1080:1920',
        `drawtext=text='${segment.title}':fontsize=24:fontcolor=white:x=(w-text_w)/2:y=100`
      ])
      .output(`/tmp/output_${videoId}_${segment.startTime}.mp4`)
      .on('end', resolve)
      .on('error', reject)
      .run();
  });
}