import random
import csv
import Adafruit_DHT
import time

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
        print('Temperature: {:.2f}°C\nHumidity: {:.2f}%'.format(temp,humid))

        if writecsv == True:
            data = [temp,humid]
            writetocsv(data, self.name)


temp1 = Sensor('DHT22-101')

for i in range(10):
    temp1.show_result(True)
    print('------')
    time.sleep(2)




