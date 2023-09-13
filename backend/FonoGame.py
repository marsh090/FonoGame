import speech_recognition as sr

# Inicialize o reconhecedor
r = sr.Recognizer()

def listen_to_microphone():
    # Capturar áudio do microfone
    with sr.Microphone() as source:
        print("Aguardando comando...")

        try:
            audio = r.listen(source, timeout=None)
            texto = r.recognize_google(audio, language='pt-BR')

            # Verificar se a palavra "Faca" foi dita e printa um emoji de faca
            if "faca" in texto.lower():
                print("Faca🔪")

            # Verificar se a palavra "Vaca" foi dita
            if "vaca" in texto.lower():
                print("Vaca🐄")

            # Verificar se a palavra "finalizar" foi dita para encerrar o programa
            if "finalizar" in texto.lower():
                print("Encerrando o programa...")
                raise KeyboardInterrupt

        except sr.UnknownValueError:
            pass  # Ignorar quando o áudio não é entendido
        except sr.RequestError as e:
            print(f"Erro na API: {e}")

if __name__ == "__main__":
    print("Pressione Ctrl+C para encerrar a captura de áudio.")
    
    try:
        while True:
            listen_to_microphone()
    except KeyboardInterrupt:
        print("\nEncerrando a captura de áudio e finalizando o programa.")
