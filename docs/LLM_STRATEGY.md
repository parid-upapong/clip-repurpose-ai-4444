# LLM Context Strategy: Hook & Highlight Extraction

## 1. Context Window Management
Since long-form transcripts can exceed token limits, we implement a **Sliding Window with Overlap** strategy. 
- Window Size: 15 minutes of transcript.
- Overlap: 2 minutes (to ensure hooks aren't cut mid-sentence between windows).

## 2. Signal-to-Noise Ratio
We preprocess transcripts to include:
- **Speaker Diarization:** Helps LLM identify who is the "Expert" vs. "Host".
- **Laughter/Applause Tags:** Injected from audio analysis to serve as "high-engagement" signals.
- **Timestamp Precision:** Timestamps every 5-10 words to ensure the LLM can provide accurate cut points.

## 3. The "Anti-Boring" Filter
The LLM is explicitly instructed to ignore:
- Generic introductions ("Hello everyone, welcome back...").
- Standard sponsorship reads.
- Technical setup talk or "Can you hear me?" segments.
- Filler words (redundant 'um's and 'ah's already stripped by Whisper).