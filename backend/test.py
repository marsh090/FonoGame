import wave

with wave.open("audio.wav", "rb") as wave_file:
    sample_rate = wave_file.getframerate()
    channels = wave_file.getnchannels()

    print(f"Taxa de amostragem: {sample_rate} Hz")
    print(f"Número de canais: {channels}")