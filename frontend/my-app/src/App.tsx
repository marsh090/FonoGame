import React, { useRef, useState } from 'react';

const App: React.FC = () => {
  const [recording, setRecording] = useState(false);
  const mediaRecorder = useRef<MediaRecorder | null>(null);
  const audioChunks = useRef<BlobPart[]>([]);

  const startRecording = () => {
    console.log("Tentando iniciar a gravação...");
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder.current = new MediaRecorder(stream);
        mediaRecorder.current.ondataavailable = event => {
          audioChunks.current.push(event.data);
        };
        mediaRecorder.current.onstop = async () => {
          const audioBlob = new Blob(audioChunks.current, { type: 'audio/wav' });
          console.log("Blob criado:", audioBlob);  // Log do blob criado
          audioChunks.current = [];
          await sendAudio(audioBlob);
        };
        mediaRecorder.current.start();
        setRecording(true);
        setTimeout(() => {
          stopRecording();
        }, 5000); // Grava por 5 segundos
      })
      .catch(err => {
        console.error("Erro ao acessar o microfone:", err);
      });
  };

  const stopRecording = () => {
    console.log("Tentando parar a gravação...");
    if (mediaRecorder.current) {
      mediaRecorder.current.stop();
      setRecording(false);
    }
  };

  const sendAudio = async (audioBlob: Blob) => {
    console.log("Tentando enviar áudio...");
    const formData = new FormData();
    formData.append('audio', audioBlob);

    try {
      const response = await fetch('http://localhost:5000/listen', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      console.log("Resposta do servidor:", data.message);
    } catch (error) {
      console.error("Erro ao enviar áudio:", error);
    }
  };

  return (
    <div>
      <button onClick={startRecording} disabled={recording}>
        Iniciar Gravação
      </button>
      <button onClick={stopRecording} disabled={!recording}>
        Parar Gravação
      </button>
    </div>
  );
};

export default App;
