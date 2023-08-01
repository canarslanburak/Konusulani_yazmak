import speech_recognition as sr

def cumleleri_belgeye_yazdir(cumleler, dosya_adi):
    with open(dosya_adi, 'w') as dosya:
        for cumle in cumleler:
            dosya.write(cumle + '\n')

r = sr.Recognizer()
cumleler = []

with sr.Microphone() as source:
    print("Mikrofon dinleniyor...")
    while True:
        try:
            audio = r.listen(source)
            cumle = r.recognize_google(audio, language='tr-TR')
            print("Algılanan cümle:", cumle)
            cumleler.append(cumle)
        except sr.UnknownValueError:
            print("Anlaşılamayan cümle")
        except sr.RequestError:
            print("Ses algılanamadı, çevrimiçi olun")

        if cumle == 'bitir':
            break

dosya_adi = input("Belge adını sonunda .txt olarak girin: ")
cumleleri_belgeye_yazdir(cumleler, dosya_adi)
