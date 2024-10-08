from elevenlabs.client import ElevenLabs
from elevenlabs import play
from ChatClient import lyrics

client = ElevenLabs(
  api_key="sk_9bad27c0e85678bc95d3304cd21bb5eb7c1ec3d2f3199fcc", # Defaults to ELEVEN_API_KEY
)

voice = client.clone(
    name="clonedVoice",
    description="Your voice should be energetic and confident, like a hip-hop artist. Speak with a rhythmic flow, almost as if you're rapping, letting the words roll smoothly. Add emphasis to key words, giving your delivery swagger and personality, similar to Snoop Dogg's laid-back yet powerful style. Maintain a dynamic yet controlled pace, making the message hit hard. Feel the vibe and convey it with emotion, turning your speech into a performance that's lively, engaging, and impossible to ignore.", # Optional
    description="Your voice should be energetic and confident, like a hip-hop artist. Speak with a rhythmic flow, almost as if you're rapping, letting the words roll smoothly. Add emphasis to key words, giving your delivery swagger and personality, similar to Snoop Dogg's laid-back yet powerful style. Maintain a dynamic yet controlled pace, making the message hit hard. Feel the vibe and convey it with emotion, turning your speech into a performance that's lively, engaging, and impossible to ignore.", # Optional
    files=["./uploads/recording.mp3"],
)

audio = client.generate(text=lyrics, voice=voice)

with open("./uploads/final_audio.mp3", "wb") as file:
    for chunk in audio:
        file.write(chunk)
        print("audio created")