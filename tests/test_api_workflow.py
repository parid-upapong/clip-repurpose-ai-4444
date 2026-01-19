import time
import pytest

def test_full_video_to_clip_lifecycle(api_client, sample_video_request):
    """
    E2E Functional Test: 
    1. Submit a long video
    2. Poll for completion
    3. Verify clips are generated with metadata
    """
    session, base_url = api_client

    # 1. Trigger Job
    response = session.post(f"{base_url}/jobs", json=sample_video_request)
    assert response.status_code == 200
    job_id = response.json()["job_id"]

    # 2. Poll Status (Max 5 minutes for AI processing)
    timeout = time.time() + 300
    status = "pending"
    
    while time.time() < timeout:
        status_resp = session.get(f"{base_url}/jobs/{job_id}")
        status = status_resp.json()["status"]
        if status in ["completed", "failed"]:
            break
        time.sleep(10)

    assert status == "completed", f"Job failed or timed out. Last status: {status}"

    # 3. Validate Output Structure
    clips_resp = session.get(f"{base_url}/jobs/{job_id}/clips")
    clips = clips_resp.json()
    
    assert len(clips) > 0, "AI failed to identify any viral hooks."
    for clip in clips:
        assert "download_url" in clip
        assert clip["virality_score"] >= 0
        assert clip["start_time"] < clip["end_time"]