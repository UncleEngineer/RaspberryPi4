from tkinter import *
from tkinter import ttk
import requests
import threading
import time

def getdata():
    url = 'http://192.168.0.183:8000/apitest'
    data = {'token':'abc1234'}
    r = requests.get(url=url,data=data)
    dataiot = r.json()[-1]
    text = 'Temperature: {} C°\n\nHumidity: {}  %\n\nUpdate: {}'.format(dataiot[1],dataiot[2],dataiot[0])
    v_text.set(text)

def run_getdata():
    while True:
        getdata()
        time.sleep(10)

GUI = Tk()
GUI.title('IOT TEMPERATURE')
GUI.state('zoomed')

v_text = StringVar()
v_text.set('Temperature: - C°\n\nHumidity: - %\n\nUpdate: -')

L = ttk.Label(GUI,textvariable=v_text,font=('tahoma',40,'bold'))
L.pack(pady=50)

task = threading.Thread(target=run_getdata)
task.start()

GUI.mainloop()