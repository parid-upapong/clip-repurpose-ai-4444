from fastapi import APIRouter, HTTPException
from .models import VideoJobRequest, JobResponse, JobDetail, JobStatus
from worker.celery_worker import process_video_task
import uuid

router = APIRouter()

# In-memory store for demo (In production, use Redis/PostgreSQL)
jobs_db = {}

@router.post("/jobs", response_model=JobResponse)
async def create_processing_job(request: VideoJobRequest):
    job_id = str(uuid.uuid4())
    
    # Initialize job state
    jobs_db[job_id] = {
        "job_id": job_id,
        "status": JobStatus.PENDING,
        "clips": []
    }
    
    # Dispatch to Celery worker for async processing
    process_video_task.delay(job_id, str(request.video_url))
    
    return JobResponse(job_id=job_id, status=JobStatus.PENDING)

@router.get("/jobs/{job_id}", response_model=JobDetail)
async def get_job_status(job_id: str):
    if job_id not in jobs_db:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return JobDetail(**jobs_db[job_id])