import ffmpeg
import cv2
import numpy as np

class VideoInspector:
    """
    Utility class to verify the physical properties of the generated AI clips.
    Ensures that the output meets platform-specific requirements (9:16 aspect ratio).
    """
    
    @staticmethod
    def get_metadata(file_path: str):
        """Extracts metadata using ffprobe."""
        probe = ffmpeg.probe(file_path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        return video_stream

    @staticmethod
    def verify_aspect_ratio(file_path: str, expected_ratio: float = 0.5625): # 9/16
        """Checks if the video dimensions match the 9:16 vertical format."""
        metadata = VideoInspector.get_metadata(file_path)
        width = int(metadata['width'])
        height = int(metadata['height'])
        actual_ratio = width / height
        # Allow a small margin for rounding errors
        assert abs(actual_ratio - expected_ratio) < 0.01, f"Invalid Aspect Ratio: {width}x{height}"

    @staticmethod
    def check_for_black_frames(file_path: str, threshold: float = 0.02):
        """
        Analyzes the video to ensure the AI haven't rendered empty/black frames.
        """
        cap = cv2.VideoCapture(file_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        black_frame_count = 0
        
        # Sample frames throughout the video
        for i in range(0, total_frames, 30):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if not ret: break
            
            if np.mean(frame) < 5: # Close to pure black
                black_frame_count += 1
                
        cap.release()
        black_ratio = black_frame_count / (total_frames / 30)
        assert black_ratio < threshold, f"Too many black frames detected: {black_ratio*100}%"