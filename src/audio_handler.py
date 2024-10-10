import os

UPLOAD_FOLDER = './src/static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

from pydub import AudioSegment

def save_audio(audio_file):
    audio_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(audio_path)
    
    # Convert to mp3
    sound = AudioSegment.from_file(audio_path)
    mp3_path = audio_path.rsplit('.', 1)[0] + ".mp3"
    sound.export(mp3_path, format="mp3")
    
    # Optionally delete the original file
    os.remove(audio_path)
    
    return mp3_path


def to_OGG(audio_file_path):
    audio_path = os.path.join(UPLOAD_FOLDER, audio_file_path)
    print(audio_path)   
    # Convert to ogg
    sound = AudioSegment.from_file(audio_path)
    ogg_path = audio_path.rsplit('.', 1)[0] + ".ogg"
    sound.export(ogg_path, format="ogg")
    
    return ogg_path