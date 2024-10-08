from elevenlabs.client import ElevenLabs
from elevenlabs import play
from moviepy.editor import concatenate_audioclips, AudioFileClip
from pydub import AudioSegment

def generate_voice(lyrics):  # Accept lyrics as a parameter
    # client = ElevenLabs(
    #     api_key="sk_9bad27c0e85678bc95d3304cd21bb5eb7c1ec3d2f3199fcc", # Defaults to ELEVEN_API_KEY
    # )

    # voice = client.clone(
    #     name="clonedVoice",
    #     description="Your voice should be energetic and confident, like a hip-hop artist. Speak with a rhythmic flow, almost as if you're rapping, letting the words roll smoothly. Add emphasis to key words, giving your delivery swagger and personality, similar to Snoop Dogg's laid-back yet powerful style. Maintain a dynamic yet controlled pace, making the message hit hard. Feel the vibe and convey it with emotion, turning your speech into a performance that's lively, engaging, and impossible to ignore.", # Optional
    #     files=["./uploads/recording.mp3"],
    # )

    # audio = client.generate(text=lyrics, voice=voice)

    # with open("./uploads/final_audio.mp3", "wb") as file:
    #     for chunk in audio:
    #         file.write(chunk)

    merge_audio()
    
    print("Audio generated successfully")

def merge_audio():
    audio1 = AudioSegment.from_file("./src/Resources/beat1.mp3")
    audio2 = AudioSegment.from_file("./uploads/final_audio.mp3")
    audio2.volume = 3
    audio1.volume = 0.5
    audio1 = audio1[:(audio2.duration_seconds * 1000)]
    final_audio = audio1.overlay(audio2)
    final_audio.export("./uploads/merged_audio.mp3", format="mp3")
