from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

r = sr.Recognizer()

@app.route('/listen', methods=['POST'])
def listen_to_microphone():
    audio_data = request.files['audio'].read()
    audio = sr.AudioData(audio_data, 16000, 2)

    try:
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
