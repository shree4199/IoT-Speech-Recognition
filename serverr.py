import socket
import RPi.GPIO as gpio
import requests
from threading import Thread
gpio.setmode(gpio.BOARD)
gpio.setup(5,gpio.OUT)
server_soc=socket.socket()
server_soc.bind(("192.168.43.159",1234))


server_soc.listen(5)
conn,addr = server_soc.accept()
def receieve_func():
    client_data = conn.recv(1000)
    print(client_data.decode())
    if client_data.decode() == "switch on the light":
        gpio.output(5,False)
        #print("SUCESSFULL")
        r = requests.post('https://maker.ifttt.com/trigger/bulb/with/key/ezxrck0MPTcReuUNIn4hzsVdu6YOgmLf4z2YMaz54y_')
    elif client_data.decode() == "switch off the light":
        gpio.output(5,True)
        r = requests.post('https://maker.ifttt.com/trigger/bulboff/with/key/ezxrck0MPTcReuUNIn4hzsVdu6YOgmLf4z2YMaz54y_')
        #print("OFF")
    


while True:
    receieve_func()
#conn.close()
