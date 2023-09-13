import speech_recognition as sr
import keyboard

# Inicialize o reconhecedor
r = sr.Recognizer()

def listen_to_microphone():
    # Capturar áudio do microfone
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Tentar reconhecer o áudio usando Google Web Speech API
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")

        # Verificar se a palavra "Faca" foi dita e printa um emoji de faca
        if "faca" in texto.lower():
            print("Faca🔪")

        # Verificar se a palavra "Vaca" foi dita
        if "vaca" in texto.lower():
            print("Vaca🐄")

    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro na API; {e}")

    # Retornar ao estado de "espera" para a próxima tentativa
    print("Pressione e segure a barra de espaço para falar novamente.")

# Definir a ação quando a barra de espaço é pressionada
keyboard.on_press_key("space", lambda _: listen_to_microphone())

print("Pressione e segure a barra de espaço para falar.")
keyboard.wait("esc")  # Aguarde até que a tecla 'esc' seja pressionada para sair
