from elevenlabs.client import ElevenLabs
from elevenlabs import play
from ChatClient import lyrics

client = ElevenLabs(
  api_key="sk_9bad27c0e85678bc95d3304cd21bb5eb7c1ec3d2f3199fcc", # Defaults to ELEVEN_API_KEY
)

voice = client.clone(
    name="clonedVoice",
    description="", # Optional
    files=["./uploads/recording.mp3"],
)

audio = client.generate(text=lyrics, voice=voice)

with open("./uploads/final_audio.mp3", "wb") as file:
    for chunk in audio:
        file.write(chunk)