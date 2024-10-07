from flask import Flask, request, render_template
from audio_handler import save_audio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_audio_route():
    if 'audio' not in request.files:
        return "No audio file provided", 400

    audio_file = request.files['audio']
    audio_path = save_audio(audio_file)
    
    return f"Saved to {audio_path}"

if __name__ == '__main__':
    app.run(debug=True)
