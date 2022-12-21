import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyautogui

escuchar = sr.Recognizer()

inicializar = pyttsx3.init()
velocidad_de_voz = 130
inicializar.setProperty('rate', velocidad_de_voz)
nombre = 'alexa'

def hablar(texto):
    inicializar.say(texto)
    inicializar.runAndWait()

def tomar_comando():
    try:
        with sr.Microphone() as voz:
            print('Escuchando...')
            voice = escuchar.listen(voz)
            command = escuchar.recognize_google(voice, language='es-ES')
            command = command.lower()
            if nombre in command:
                command = command.replace(nombre, '')
                print(command)
    except:
        pass
    return command

def alexa():
    command = tomar_comando()
    if 'reproduce' in command:
        cancion = command.replace('reproduce', '')
        hablar('Reproduciendo ' + cancion)
        pywhatkit.playonyt(cancion)
        
    elif 'hora' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        hablar('Son las ' + time)
        print(time)
    
    elif "wikipedia" in command:
        busqueda = command.replace("wikipedia", "")
        informacion = wikipedia.set_lang("es")
        informacion = wikipedia.summary(busqueda, 1)
        hablar(informacion)
        print(informacion)
    
    elif "pantalla" in command:
        screenshot = pyautogui.screenshot()
        screenshot.save("Screenshot.png")
        hablar("Captura de pantalla realizada")
    
    else:
        hablar("No te entiendo, repite por favor")
        
alexa()
    
