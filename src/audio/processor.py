from .stt_engine import TranscriptionEngine
from .caption_sync import CaptionGenerator
from moviepy.editor import VideoFileClip, CompositeVideoClip

class AudioVisualIntegrator:
    """
    The orchestrator that binds Audio, Neural TTS, and Captions to the Video stream.
    """
    def __init__(self):
        self.stt = TranscriptionEngine()
        self.captioner = CaptionGenerator()

    def process_video_audio_stack(self, video_path: str, output_path: str):
        # 1. Extract and Transcribe
        video = VideoFileClip(video_path)
        audio_path = "temp_audio.wav"
        video.audio.write_audiofile(audio_path)
        
        word_segments = self.stt.transcribe_with_word_timestamps(audio_path)
        
        # 2. Create Caption Clips
        caption_clips = self.captioner.generate_caption_layer(word_segments)
        
        # 3. Composite and Render
        final_video = CompositeVideoClip([video] + caption_clips)
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        
        print(f"Successfully processed video with synced captions: {output_path}")