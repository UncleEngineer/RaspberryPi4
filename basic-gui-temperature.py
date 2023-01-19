from tkinter import *

#####################TEMPERATURE######################
import random
import csv
import Adafruit_DHT
import time
import threading

def writetocsv(data,filename='data'):
    # data = [25.66,50.66]
    with open('{}.csv'.format(filename) ,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

class Sensor:
    """ Sensor Class for IoT """
    def __init__(self,name='DF-101'):
        self.name = name
        self.type = 'DHT22'
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 2

    def get_temp_humid(self):
        h, t = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
        return (round(t,2),round(h,2))

    def show_result(self, writecsv=False):
        temp, humid = self.get_temp_humid()
        #print('Temperature: {:.2f}°C\nHumidity: {:.2f}%'.format(temp,humid))

        if writecsv == True:
            data = [temp,humid]
            writetocsv(data, self.name)

###########################################

GUI = Tk()
GUI.title('Temperature Monitoring')
GUI.geometry('500x400+50+50')
GUI.attributes('-fullscreen',True)

GUI.bind('<F1>',lambda x: GUI.attributes('-fullscreen',False))
GUI.bind('<F2>',lambda x: GUI.attributes('-fullscreen',True))

FONT1 = (None,80)
FONT2 = (None,80,'bold')

L = Label(GUI,text='Temperature',font=FONT1)
L.pack(pady=40)

# Temperature 20°C
v_temperature = StringVar()
v_temperature.set('XX.YY °C')

L = Label(GUI, textvariable=v_temperature, font=FONT2, fg='blue')
L.pack(pady=40)

temperature = 20


def AddTemp():
    global temperature
    temperature += 1
    #print(temperature)
    v_temperature.set('{:.2f} °C'.format(temperature))


def UpdateTemp():
    global temperature
    sensor = Sensor()
    t,h = sensor.get_temp_humid()
    temperature = t
    v_temperature.set('{:.2f} °C'.format(temperature))
    #print('updated')

def RunUpdateTemp():
    while True:
        try:
            UpdateTemp()
        except:
            v_temperature.set('ERROR')
        time.sleep(10)


B = Button(GUI,text='Update',command=UpdateTemp)
B.pack()


task = threading.Thread(target=RunUpdateTemp)
task.start()


#L.place(x=50,y=100)

GUI.mainloop()

