import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
import time
duration = 5  # seconds of recording
sample_rate = 44100
seviyeye_gore_kelimeler = {
    "kolay": ["cat", "dog", "apple", "hello", "sun"],
    "orta": ["banana", "school", "friend", "window", "yellow"],
    "zor": ["resilient", "receive", "avoid", "pronunciation", "achieve"]
}
score=0
print("lütfen bir zorluk seçiniz:kolay,orta,zor")
seviye=input(">>>")
kelime_listesi=seviyeye_gore_kelimeler[seviye]
random.shuffle(kelime_listesi)
print("ingilizce bir kelime göreceksiniz ve onu telaffuz etmeniz gerekecektir.")
time.sleep(2)
for kelime in kelime_listesi:
    print(f"telaffuz etmeniz gereken kelime şudur:{kelime}")
    print("konuşabilirsiniz lütfen")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    wav.write("output.wav", sample_rate, recording)
    print("✅ Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en")
        print("📝 Şunu söylediniz:", text)
        if text==kelime:
            print("bravo! bu kelimeyi doğru telaffuz ettiniz:)")
            score+=1
        else:
            print("maalesef yanlış yaptınnn:()")
    except sr.UnknownValueError:
        print("😕 Konuşma tanınamadı.")
    except sr.RequestError as e:
        print(f"❗ Hizmet hatası: {e}")
    time.sleep(2)
print(f"oyun bitti skorunuz :{score}")
