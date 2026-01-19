import numpy as np

class SmartReframer:
    """
    Calculates the 9:16 crop window with cinematic smoothing.
    """
    def __init__(self, width, height, smoothing_factor=0.1):
        self.original_w = width
        self.original_h = height
        self.target_ratio = 9 / 16
        self.target_w = int(height * self.target_ratio)
        self.target_h = height
        
        # Current window center X (normalized 0 to 1)
        self.current_center_x = 0.5
        self.smoothing_factor = smoothing_factor

    def calculate_crop(self, focus_x):
        """
        Calculates the bounding box for the 9:16 crop.
        focus_x: The normalized X coordinate of the speaker (0.0 to 1.0).
        """
        if focus_x is None:
            focus_x = 0.5 # Default to center

        # Apply smoothing (Linear Interpolation) to prevent jerky camera movements
        self.current_center_x = (
            self.current_center_x * (1 - self.smoothing_factor) + 
            focus_x * self.smoothing_factor
        )

        # Convert normalized center to pixel coordinate
        pixel_center_x = int(self.current_center_x * self.original_w)

        # Calculate crop bounds
        x1 = pixel_center_x - (self.target_w // 2)
        x2 = x1 + self.target_w

        # Edge handling: ensure crop stays within original video frame
        if x1 < 0:
            x1 = 0
            x2 = self.target_w
        elif x2 > self.original_w:
            x2 = self.original_w
            x1 = x2 - self.target_w

        return x1, 0, x2, self.original_h

    def get_crop_tuple(self, focus_x):
        """Returns (x1, y1, x2, y2)"""
        return self.calculate_crop(focus_x)