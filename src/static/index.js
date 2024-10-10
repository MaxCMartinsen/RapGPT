const recordButton = document.getElementById('recordButton');
const beatButton = document.getElementById('beatcb');
const cloneButton = document.getElementById('clonecb');
const sourceAudio = document.getElementById('srcAudio');
const status = document.getElementById('status');
let mediaRecorder;
let audioChunks = [];

let recording = false

recordButton.addEventListener('click', () => {
    if (recording === false) {
        recording = true
        startRecording();
    } else {
        recording = false
        stopRecording();
    }
});

beatButton.addEventListener('click', () => {
    if (beatButton.checked) {
        sourceAudio.src = "{{ url_for('static', filename='uploads/merged_audio.mp3') }}";
        console.log("Playing merged audio (beat)");
    } else {
        sourceAudio.src = "{{ url_for('static', filename='uploads/final_audio.mp3') }}";
        console.log("Playing final audio (no beat)");
    }
    sourceAudio.load();
    sourceAudio.play();
});


function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();
            recordButton.textContent = "Stop Recording";
            status.textContent = "Recording...";


            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
                const formData = new FormData();
                formData.append('audio', audioBlob, 'recording.webm');
                
                fetch('/save', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.text())
                .then(data => {
                    status.textContent = "Generating rap...";
                    console.log("Audio saved:", data);
                })
                .catch(error => {
                    status.textContent = "Error saving recording.";
                    console.error("Error:", error);
                });
                
                audioChunks = [];
            };
        })
        .catch(error => {
            console.error("Error accessing microphone:", error);
        });
}

function stopRecording() {
    mediaRecorder.stop();
    recordButton.textContent = "Start Recording";
    status.textContent = "Processing...";
}
