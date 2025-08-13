
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY


elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str, folder: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = elevenlabs.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    folder_path = os.path.join("user_uploads", folder)
    os.makedirs(folder_path, exist_ok=True)
    save_file_path = os.path.join(folder_path, "audio.mp3")

    # Save the input text to desc.txt in the same folder
    desc_file_path = os.path.join(folder_path, "desc.txt")
    with open(desc_file_path, "w", encoding="utf-8") as desc_file:
        desc_file.write(text)

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

# text_to_speech_file("Hi This is a new test and I am very excited to see how it will work!", "text_audio_file")