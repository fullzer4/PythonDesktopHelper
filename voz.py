import speech_recognition as sr
import pyttsx3
import datetime
import hora from

rec = sr.Recognizer()
gigi = pyttsx3.init()

def executarComandos():
    try:
        with sr.Microphone(device_index=2) as mic: # 2 desktop e 8 notebook Ubuntu
            rec.adjust_for_ambient_noise(mic)
            print("Ouvindo")
            audio = rec.listen(mic)
            frase = rec.recognize_google(audio, language="pt-BR")
            print(frase)
            if "gigi" in frase:
                frase = frase.replace("gigi", "")
            return frase

    except:
        return "nada"

def comandoUser():
    frase = executarComandos()
    print("a")
    if "nada" in frase:
        return
    elif "horas" in frase:
        hora = datetime.datetime.now().strftime("%H:%M")
        print("foi " + hora)
        gigi.say("Ola lindo")
        gigi.say("São"+hora)
        gigi.runAndWait()
    else:
        return

while True:
    comandoUser()