from openai import OpenAI
from pathlib import Path
import os
apikey = os.getenv("rapgpt_api")
client = OpenAI(api_key=apikey)
audio_file= open("C:/repos/HorizonAI/RapGPT/uploads/recording.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": transcription.text},
    {"role": "user", "content": "Answer the sentence in rap"}
  ]
)
lyrics = completion.choices[0].message.content
print(lyrics)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="onyx",
  input=lyrics,
  speed="1.2"
)

response.stream_to_file(speech_file_path)