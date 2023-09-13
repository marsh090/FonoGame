from flask import Flask, request, jsonify
from flask_cors import CORS  # Importe o CORS
import speech_recognition as sr

app = Flask(__name__)
CORS(app, resources={r"/listen": {"origins": "http://localhost:3000"}})

app = Flask(__name__)

r = sr.Recognizer()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/listen', methods=['POST'])
def listen_to_microphone():
    print("Requisição recebida:", request.files)
    audio_data = request.files['audio'].read()
    audio = sr.AudioData(audio_data, 16000, 2)

    try:
        with open("received_audio.wav", "wb") as f:
            f.write(audio_data)
        texto = r.recognize_google(audio, language='pt-BR')
        if "faca" in texto.lower():
            return jsonify({"message": "Faca🔪"})
        elif "vaca" in texto.lower():
            return jsonify({"message": "Vaca🐄"})
        else:
            return jsonify({"message": f"Você disse: {texto}"})
    except sr.UnknownValueError:
        return jsonify({"message": "Não foi possível entender o áudio."})
    except sr.RequestError as e:
        return jsonify({"message": f"Erro na API; {e}"})

if __name__ == '__main__':
    app.run(debug=True)
