import moviepy.editor as mp
from cv.face_engine import FaceEngine # Reusing the module from project context
import numpy as np

class RenderService:
    """
    Handles the actual video manipulation: 
    Cropping to 9:16 and applying AI-driven reframing.
    """
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.face_engine = FaceEngine()

    def render_short_clip(self, source_url: str, start: float, end: float, index: int):
        """
        Extracts a segment and transforms it to 9:16 vertical format.
        """
        # Note: In production, source_url would be a local path after download
        video = mp.VideoFileClip(source_url).subclip(start, end)
        
        # Target Dimensions for TikTok/Reels
        target_w, target_h = 1080, 1920
        source_w, source_h = video.size
        
        def smart_crop_frame(get_frame, t):
            frame = get_frame(t)
            # Use FaceEngine to find the speaker's horizontal center
            # We pass a sample of the frame to get the focus point
            focus_x = self.face_engine.get_speaker_focus(frame) 
            
            # Calculate cropping coordinates
            # Center the crop on the detected speaker, keeping bounds safe
            half_width = (source_h * (9/16)) / 2
            left = max(0, min(source_w - 2*half_width, focus_x - half_width))
            right = left + (2 * half_width)
            
            return frame[:, int(left):int(right)]

        # Apply the dynamic cropping transformation
        short_video = video.fl(smart_crop_frame, apply_to=['mask', 'video'])
        short_video = short_video.resize(height=target_h)
        
        output_filename = f"exports/clip_{self.job_id}_{index}.mp4"
        # In production, upload this to S3
        short_video.write_videofile(output_filename, codec="libx264", audio_codec="aac")
        
        return output_filename