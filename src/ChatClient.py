from flask import Flask, request
import os
from openai import OpenAI
from pathlib import Path
from Voice_handler import generate_voice

def generate_lyrics():
    # Initialize API client
    apikey = os.getenv("rapgpt_api")
    client = OpenAI(api_key=apikey)
    
    # Define paths
    audio_file_path = Path("./uploads/recording.mp3")
    speech_file_path = Path(__file__).parent / "speech.mp3"

    try:
        # Transcription
        with audio_file_path.open("rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            text = transcription.text
            print(text)

        # Generate lyrics in rap style
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": text},
<<<<<<< HEAD
                {"role": "user", "content": "Answer the sentence in rap"}
=======
                {"role": "user", "content": "Answer the sentence in rap; make a description (max 200 charaters) for a beat that you would like to use for the rap; and response in json, lyrics called lyrics, and description called description."}
>>>>>>> 9ab3829fb4462ae3faee7e944c0e176391532bd8
            ]
        )
        lyrics = completion.choices[0].message.content
        lyrics = json.loads["lyrics"]
        print(lyrics)
<<<<<<< HEAD
=======
        # description = json.loads(completion.choices[0].message.content)
        # description = description["description"]
        # lyrics = description["lyrics"]
        # print(description)
>>>>>>> 9ab3829fb4462ae3faee7e944c0e176391532bd8

        # Generate and save speech
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="onyx",
            input=lyrics,
            speed="1.2"
        )
        response.stream_to_file(speech_file_path)
        print("Lyrics generated and saved successfully")

        # Additional voice handling
        generate_voice(lyrics)

    except Exception as e:
        print(f"An error occurred: {e}")
