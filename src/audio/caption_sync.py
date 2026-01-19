from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
import numpy as np

class CaptionGenerator:
    """
    Synchronizes transcribed words into 'Karaoke-style' dynamic captions.
    """
    def __init__(self, video_size=(1080, 1920), font_path=None):
        self.w, self.h = video_size
        self.font = font_path or "Arial-Bold"

    def create_word_clip(self, word_data: dict, is_active: bool = False):
        """
        Creates a single word clip. Highlights if 'is_active'.
        """
        color = 'yellow' if is_active else 'white'
        size = 80 if is_active else 70
        
        return TextClip(
            word_data['word'].upper(),
            fontsize=size,
            color=color,
            font=self.font,
            stroke_color='black',
            stroke_width=2,
            method='caption',
            size=(self.w * 0.8, None)
        ).set_start(word_data['start']).set_duration(word_data['end'] - word_data['start'])

    def generate_caption_layer(self, word_segments: list):
        """
        Generates a sequence of clips that highlight words as they are spoken.
        """
        clips = []
        for i, word in enumerate(word_segments):
            # Centering logic for vertical video (9:16)
            txt_clip = self.create_word_clip(word, is_active=True)
            # Position at the lower third
            txt_clip = txt_clip.set_position(('center', self.h * 0.7))
            clips.append(txt_clip)
            
        return clips