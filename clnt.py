import speech_recognition as sr

import socket
from threading import Thread
audio = ""
r = sr.Recognizer()


client_soc =socket.socket()
client_soc.connect(("192.168.43.159",1234))


def send_func():
    with sr.Microphone() as spurce:
        print("Say Somethig")
        audio = r.listen(spurce)
        aud = str(audio)
    try:
        print(r.recognize_google(audio))


    except:
        pass




        #user_input = input()
    client_soc.sendall(r.recognize_google(audio).encode())



while True:
    send_func()


