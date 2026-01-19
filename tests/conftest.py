import pytest
import os
import requests
from typing import Generator

# Configuration for the test environment
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
TEST_VIDEO_URL = "https://storage.googleapis.com/overlord-test-assets/raw_podcast_sample.mp4"

@pytest.fixture(scope="session")
def api_client():
    """
    Fixture to provide a base URL and shared session for API testing.
    """
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session, API_BASE_URL

@pytest.fixture
def sample_video_request():
    """
    Standard request payload for creating a video processing job.
    """
    return {
        "video_url": TEST_VIDEO_URL,
        "target_platforms": ["tiktok", "reels"],
        "detect_speakers": True
    }