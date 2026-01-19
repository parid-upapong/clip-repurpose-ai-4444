from fastapi import FastAPI, HTTPException, BackgroundTasks
from .models import VideoJobRequest, JobResponse, JobDetail, JobStatus
from .router import router as job_router
import uuid

app = FastAPI(
    title="OVERLORD AI API Gateway",
    description="Backend services for automated video repurposing",
    version="1.0.0"
)

# Include specialized routes
app.include_router(job_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "operational"}