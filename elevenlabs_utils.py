from elevenlabs import set_api_key
from elevenlabs import generate, play, clone, voices
from dotenv import load_dotenv
import os

load_dotenv()

set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def list_available_voices():
    """Lists available voices"""
    return voices()

def generate_audio(text: str):
    """Generates audio from text"""
    audio = generate(
        text=text,
        voice="8elFlXC7xvaU72IGbroZ",
        model="eleven_multilingual_v2"
    )
    return audio

def generate_cloned_audio(text: str, file_sample_directory: str):
    """Generates cloned audio from text and a file sample directory"""
    # From the file_sample_directory, get the list of mp3 files
    # and pass it to the clone function
    files = [file_sample_directory + file for file in os.listdir(file_sample_directory) if file.endswith(".mp3")]

    voice = clone(
        name="Gleb",
        description="A young male",
        files=files
    )

    audio = generate(text=text, voice=voice)
    play(audio)

if __name__ == "__main__":
    print(generate_audio("Hello world!"))