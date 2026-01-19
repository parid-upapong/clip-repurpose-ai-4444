import cv2
import mediapipe as mp
import numpy as np

class FaceEngine:
    """
    Detects faces and identifies the primary speaker using facial landmarks.
    """
    def __init__(self, confidence=0.5):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_face_mesh = mp.solutions.face_mesh
        self.detector = self.mp_face_detection.FaceDetection(
            model_selection=1, min_detection_confidence=confidence
        )
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=5, refine_landmarks=True, min_detection_confidence=confidence
        )

    def get_speaker_focus(self, frame):
        """
        Analyzes frame to find all faces and identifies the 'Active' speaker 
        based on mouth movement (lip distance).
        """
        results = self.face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        faces = []
        
        if not results.multi_face_landmarks:
            return None

        for face_landmarks in results.multi_face_landmarks:
            # Calculate Lip Distance (landmark 13 and 14 are inner lips)
            upper_lip = face_landmarks.landmark[13]
            lower_lip = face_landmarks.landmark[14]
            lip_dist = abs(upper_lip.y - lower_lip.y)
            
            # Get face center (Nose tip is landmark 1)
            nose = face_landmarks.landmark[1]
            
            faces.append({
                "center_x": nose.x,
                "center_y": nose.y,
                "lip_dist": lip_dist
            })

        # Identify active speaker: The one with the highest lip movement 
        # (or simply the most prominent face if no one is clearly talking)
        active_speaker = max(faces, key=lambda x: x['lip_dist'])
        return active_speaker