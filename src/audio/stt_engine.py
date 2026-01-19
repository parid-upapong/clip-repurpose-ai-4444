import whisper
import json
from typing import List, Dict

class TranscriptionEngine:
    """
    Handles speech-to-text with word-level timestamps for precise caption synchronization.
    """
    def __init__(self, model_size="base"):
        # Using Whisper for robust multilingual transcription
        self.model = whisper.load_model(model_size)

    def transcribe_with_word_timestamps(self, audio_path: str) -> List[Dict]:
        """
        Transcribes audio and returns word-level timing data.
        Format: [{'word': 'Hello', 'start': 0.1, 'end': 0.4}, ...]
        """
        result = self.model.transcribe(audio_path, word_timestamps=True)
        word_segments = []
        
        for segment in result['segments']:
            for word_data in segment['words']:
                word_segments.append({
                    "word": word_data['word'].strip(),
                    "start": word_data['start'],
                    "end": word_data['end'],
                    "probability": word_data['probability']
                })
        
        return word_segments

    def save_segments_to_json(self, segments: List[Dict], output_path: str):
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(segments, f, indent=4, ensure_ascii=False)