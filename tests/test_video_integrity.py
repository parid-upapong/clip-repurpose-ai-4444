import pytest
import requests
import os
from tests.utils.video_inspector import VideoInspector

def test_output_media_integrity(api_client):
    """
    Integration Test: 
    Downloads the actual AI-generated .mp4 and verifies 
    it is correctly cropped for TikTok/Reels.
    """
    session, base_url = api_client
    
    # Get the latest completed job
    recent_jobs = session.get(f"{base_url}/jobs?limit=1&status=completed").json()
    if not recent_jobs:
        pytest.skip("No completed jobs found to verify integrity.")
        
    job_id = recent_jobs[0]["job_id"]
    clips = session.get(f"{base_url}/jobs/{job_id}/clips").json()
    clip_url = clips[0]["download_url"]
    
    # Download locally for inspection
    local_filename = f"temp_clip_{job_id}.mp4"
    with requests.get(clip_url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    try:
        inspector = VideoInspector()
        # Ensure it is 9:16
        inspector.verify_aspect_ratio(local_filename)
        # Ensure AI didn't output "dead" video
        inspector.check_for_black_frames(local_filename)
        
        # Platform specific constraint: Clips should be < 60s for standard Reels
        metadata = inspector.get_metadata(local_filename)
        duration = float(metadata['duration'])
        assert duration <= 60.0, f"Clip is too long for short-form platforms: {duration}s"
        
    finally:
        if os.path.exists(local_filename):
            os.remove(local_filename)