const recordButton = document.getElementById('recordButton');
const status = document.getElementById('status');
let mediaRecorder;
let audioChunks = [];


recordButton.addEventListener('click', () => {
    if (recordButton.textContent === "Start Recording") {
        startRecording();
    } else {
        stopRecording();
    }
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
                    status.textContent = "Recording saved!";
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
