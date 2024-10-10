from flask import Flask, request, render_template, send_from_directory
from audio_handler import save_audio
import ChatClient as cc
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_audio_route():
    if 'audio' not in request.files:
        return "No audio file provided", 400

    audio_file = request.files['audio']
    audio_path = save_audio(audio_file)
    cc.generate_lyrics()
    return f"Saved to {audio_path}"

from flask import Flask, request, render_template, send_from_directory
from audio_handler import save_audio
import ChatClient as cc
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_audio_route():
    if 'audio' not in request.files:
        return "No audio file provided", 400

    audio_file = request.files['audio']
    audio_path = save_audio(audio_file)
    cc.generate_lyrics()
    return f"Saved to {audio_path}"


@app.route('/src/static/uploads/<path:filename>')
def serve_audio(filename):
    print("don")
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug=True)

