import os
from elevenlabs import generate, save, set_api_key
from typing import Optional

class NeuralVoiceSynthesizer:
    """
    Integrates High-Fidelity Neural TTS (ElevenLabs) for AI narration or voice replacement.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        if self.api_key:
            set_api_key(self.api_key)

    def generate_narration(self, text: str, voice_id: str = "Rachel", model: str = "eleven_multilingual_v2"):
        """
        Generates high-quality neural audio for a given text string.
        """
        try:
            audio = generate(
                text=text,
                voice=voice_id,
                model=model
            )
            return audio
        except Exception as e:
            print(f"Error generating neural voice: {e}")
            return None

    def export_audio(self, audio_bytes: bytes, output_path: str):
        if audio_bytes:
            save(audio_bytes, output_path)
            return output_path
        return None