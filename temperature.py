import random
import csv
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

##########LCDLIB###########
import lcdlib
lcd = lcdlib.lcd()
############RELAY############
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay = 17 # GPIO17
GPIO.setup(relay, GPIO.OUT)


def writetocsv(data,filename='data'):
    # data = [25.66,50.66]
    with open('{}.csv'.format(filename) ,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
        
def TurnOn(sleep=0):
    GPIO.output(relay, False)
    if sleep > 0:
        time.sleep(sleep)
        
def TurnOff(sleep=0):
    GPIO.output(relay, True)
    if sleep > 0:
        time.sleep(sleep)

# TurnOff at Start
TurnOff()


class Sensor:
    """ Sensor Class for IoT """
    def __init__(self,name='DF-101'):
        self.name = name
        self.type = 'DHT22'
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 27
        self.current_temp = 0
        self.current_humid = 0

    def get_temp_humid(self):
        h, t = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
        return (round(t,2),round(h,2))

    def show_result(self, writecsv=False):
        temp, humid = self.get_temp_humid()
        self.current_temp = temp
        self.current_humid = humid
        #
        text_temp = 'Temp: {:.2f}-C'.format(temp)
        text_humid = 'Humid: {:.2f}%'.format(humid)
        #print(text_temp)
        lcd.lcd_display_string(text_temp,1)
        lcd.lcd_display_string(text_humid,2)
        #print('Temperature: {:.2f}°C\nHumidity: {:.2f}%'.format(temp,humid))

        if writecsv == True:
            data = [temp,humid]
            writetocsv(data, self.name)


temp1 = Sensor('DHT22-101')

while True:
    try:
        temp1.show_result(True)
        if temp1.current_temp >= 30:
            TurnOn()
        else:
            TurnOff()
    except:
        pass
    #print('------')
    time.sleep(2)




