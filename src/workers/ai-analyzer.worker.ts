import { Worker, Job } from 'bullmq';
import { PipelineEvent, ClipsIdentifiedPayload } from '../shared/events';
import OpenAI from 'openai';

const openai = new OpenAI();

/**
 * Worker responsible for analyzing transcripts to find viral moments
 */
const aiWorker = new Worker('video-pipeline', async (job: Job) => {
  if (job.name === PipelineEvent.TRANSCRIPTION_COMPLETED) {
    const { videoId, transcript } = job.data;

    const completion = await openai.chat.completions.create({
      model: "gpt-4-turbo-preview",
      messages: [
        { 
          role: "system", 
          content: "You are a viral content strategist. Analyze the transcript and return a JSON array of the most engaging clips (15-60s). Identify hooks, punchlines, and high-value insights." 
        },
        { role: "user", content: transcript }
      ],
      response_format: { type: "json_object" }
    });

    const segments = JSON.parse(completion.choices[0].message.content!).clips;

    // Pass to next stage: The Editor
    await job.queue.add(PipelineEvent.CLIPS_IDENTIFIED, {
      videoId,
      segments
    } as ClipsIdentifiedPayload);
  }
}, { connection: { host: 'redis', port: 6379 } });