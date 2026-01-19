from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum

class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class VideoJobRequest(BaseModel):
    video_url: HttpUrl
    target_platforms: List[str] = ["tiktok", "reels"]
    detect_speakers: bool = True

class JobResponse(BaseModel):
    job_id: str
    status: JobStatus

class ClipMetadata(BaseModel):
    clip_id: str
    start_time: float
    end_time: float
    virality_score: float
    download_url: Optional[str] = None
    thumbnail_url: Optional[str] = None

class JobDetail(JobResponse):
    clips: List[ClipMetadata] = []
    error_message: Optional[str] = None