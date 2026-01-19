import os
import json
from typing import Dict, Any
from openai import OpenAI
from .schemas import ExtractionResponse

class ViralHighlightService:
    """
    Service responsible for interacting with LLMs to identify
    viral hooks and highlights from transcripts.
    """
    
    def __init__(self, api_key: str = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4-turbo-preview" # Using high-reasoning model for context

    def get_system_prompt(self) -> str:
        # Load the prompt from the markdown file
        with open("prompts/hook_extraction_system.md", "r") as f:
            return f.read()

    async def analyze_transcript(self, transcript_json: str) -> ExtractionResponse:
        """
        Sends transcript to LLM and returns structured clip data.
        transcript_json: List of dicts with {start, end, text, speaker}
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.get_system_prompt()},
                {"role": "user", "content": f"Analyze this transcript for viral clips:\n\n{transcript_json}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.2 # Lower temperature for consistent extraction logic
        )

        raw_content = response.choices[0].message.content
        return ExtractionResponse.model_validate_json(raw_content)

    def format_output_for_video_engine(self, extraction: ExtractionResponse) -> Dict[str, Any]:
        """
        Formats the LLM output into instructions for the MoviePy/FFmpeg engine.
        """
        return {
            "version": "1.0",
            "metadata": {
                "summary": extraction.video_summary,
                "virality_index": extraction.potential_virality_index
            },
            "tasks": [
                {
                    "start": clip.start_time,
                    "end": clip.end_time,
                    "overlays": clip.on_screen_text,
                    "caption": clip.suggested_caption
                } for clip in extraction.clips
            ]
        }