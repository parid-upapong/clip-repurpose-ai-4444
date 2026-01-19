from typing import List, Optional
from pydantic import BaseModel, Field

class HighlightClip(BaseModel):
    title: str = Field(..., description="A catchy internal title for the clip")
    start_time: float = Field(..., description="Start time in seconds")
    end_time: float = Field(..., description="End time in seconds")
    duration: float
    hook_description: str = Field(..., description="Detailed explanation of why the first 5 seconds work")
    virality_score: int = Field(..., ge=1, le=10)
    suggested_caption: str
    on_screen_text: List[str] = Field(..., description="Key phrases for visual text overlays")
    rationale: str = Field(..., description="Why this segment was chosen over others")

class ExtractionResponse(BaseModel):
    video_summary: str
    potential_virality_index: float
    clips: List[HighlightClip]
    target_audience: List[str]