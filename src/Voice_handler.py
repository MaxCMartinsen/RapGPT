from elevenlabs.client import ElevenLabs
from elevenlabs import play
import elevenlabs
from moviepy.editor import concatenate_audioclips, AudioFileClip
from pydub import AudioSegment
from flask import Flask, request, jsonify
from flask_cors import CORS
import audio_handler as ah
app = Flask(__name__)
CORS(app)

beat = False

import requests



def generate_voice(lyrics):  # Accept lyrics as a parameter
    client = ElevenLabs(
        api_key="sk_5ebfe0d699658a5de0dcc3cfe8b2394a0ac87a6ffbfd1500", # Defaults to ELEVEN_API_KEY
    )

    voice = client.clone(
        

        name="clonedVoice",
        description="Your voice should be energetic and confident, like a hip-hop artist. Speak with a rhythmic flow, almost as if you're rapping, letting the words roll smoothly. Add emphasis to key words, giving your delivery swagger and personality, similar to Snoop Dogg's laid-back yet powerful style. Maintain a dynamic yet controlled pace, making the message hit hard. Feel the vibe and convey it with emotion, turning your speech into a performance that's lively, engaging, and impossible to ignore.", # Optional
        files=["./src/static/uploads/recording.mp3"]
       

    )
   

    audio = client.generate(text=lyrics, voice=voice)
    with open("./src/static/uploads/final_audio.mp3", "wb") as file:
        for chunk in audio:
            file.write(chunk)
        merge_audio()
        ah.to_OGG("./merged_audio.mp3")
        
    
    print("Audio generated successfully")

    print("this is the voice id: " + voice.voice_id)
   
   

    url = "https://api.elevenlabs.io/v1/voices/" + voice.voice_id
    headers = {"xi-api-key": "sk_5ebfe0d699658a5de0dcc3cfe8b2394a0ac87a6ffbfd1500"}
    response = requests.request("DELETE", url, headers=headers)
    print(123)
    print(response.text)

def merge_audio():
    audio1 = AudioSegment.from_file("./src/Resources/beat1.mp3")
    audio2 = AudioSegment.from_file("./src/static/uploads/final_audio.mp3")
    audio2_louder = audio2 + 5
    audio1_quieter = audio1 - 5
    audio1_quieter = audio1_quieter[:(audio2_louder.duration_seconds * 1000)]
    final_audio = audio1_quieter.overlay(audio2_louder)
    final_audio.export("./src/static/uploads/merged_audio.mp3", format="mp3")
    print("Audio merged successfully")

