from pydub import AudioSegment

class AudioMixer:
    """
    Handles audio ducking and blending between original speech, 
    neural voiceovers, and background music.
    """
    @staticmethod
    def blend_audio_with_bgm(speech_path: str, music_path: str, output_path: str, music_volume_db: int = -15):
        """
        Mixes speech with background music, reducing music volume automatically.
        """
        speech = AudioSegment.from_file(speech_path)
        music = AudioSegment.from_file(music_path)

        # Loop music if shorter than speech
        if len(music) < len(speech):
            music = music * (len(speech) // len(music) + 1)
        
        music = music[:len(speech)] + music_volume_db
        
        # Overlay speech on top of music
        combined = music.overlay(speech)
        combined.export(output_path, format="mp3")
        return output_path