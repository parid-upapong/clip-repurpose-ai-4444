import cv2
from .face_engine import FaceEngine
from .reframer_logic import SmartReframer

class VideoProcessor:
    """
    Main pipeline for converting 16:9 video to 9:16 with AI tracking.
    """
    def __init__(self, input_path, output_path):
        self.cap = cv2.VideoCapture(input_path)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        
        self.engine = FaceEngine()
        self.reframer = SmartReframer(self.width, self.height)
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(
            output_path, 
            fourcc, 
            self.fps, 
            (self.reframer.target_w, self.reframer.target_h)
        )

    def process(self):
        print(f"Starting Smart Reframing: {self.width}x{self.height} -> 9:16")
        
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # 1. AI Analysis: Find the speaker
            speaker = self.engine.get_speaker_focus(frame)
            focus_x = speaker['center_x'] if speaker else 0.5
            
            # 2. Reframing: Calculate smooth crop
            x1, y1, x2, y2 = self.reframer.get_crop_tuple(focus_x)
            
            # 3. Execution: Crop the frame
            cropped_frame = frame[y1:y2, x1:x2]
            
            # Optional: Resize if slightly off due to rounding
            final_frame = cv2.resize(cropped_frame, (self.reframer.target_w, self.reframer.target_h))
            
            self.out.write(final_frame)

        self.cap.release()
        self.out.release()
        print("Processing Complete.")

if __name__ == "__main__":
    import sys
    processor = VideoProcessor(sys.argv[1], "output_short.mp4")
    processor.process()