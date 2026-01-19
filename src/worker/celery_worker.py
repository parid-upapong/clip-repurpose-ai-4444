import os
from celery import Celery
from .render_service import RenderService

# Configuration
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "video_workers",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

@celery_app.task(name="process_video_task", bind=True)
def process_video_task(self, job_id: str, video_url: str):
    """
    Main background task that orchestrates:
    1. Download
    2. AI Transcription & Hook Detection (Mocked here)
    3. CV-based Smart Framing
    4. Async Rendering
    """
    renderer = RenderService(job_id)
    
    try:
        # Update status to processing
        # In production, use a shared DB (SQLAlchemy) to update state
        print(f"Starting job {job_id} for {video_url}")
        
        # 1. Logic for highlight detection (Simplified)
        highlights = [
            {"start": 10.0, "end": 40.0, "score": 0.95},
            {"start": 120.5, "end": 150.5, "score": 0.88}
        ]
        
        # 2. Trigger rendering for each highlight
        processed_clips = []
        for i, clip_data in enumerate(highlights):
            clip_path = renderer.render_short_clip(
                video_url, 
                clip_data["start"], 
                clip_data["end"], 
                index=i
            )
            processed_clips.append({
                "clip_id": f"{job_id}_{i}",
                "start_time": clip_data["start"],
                "end_time": clip_data["end"],
                "virality_score": clip_data["score"],
                "download_url": clip_path
            })
            
        return {"status": "completed", "clips": processed_clips}
        
    except Exception as e:
        print(f"Job {job_id} failed: {str(e)}")
        return {"status": "failed", "error": str(e)}