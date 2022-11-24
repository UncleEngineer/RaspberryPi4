import random

def Hello():
    print('Hello World')

# Hello()

def random_temperature():
    t = random.uniform(25,39)
    t = round(t,2)
    return t

def random_humidity():
    h = random.uniform(50,95)
    h = round(h,2)
    return h

def random_mix():
    t = random.uniform(25,39)
    t = round(t,2)
    h = random.uniform(50,95)
    h = round(h,2)
    return (t,h)

def random_mix_dict():
    t = random.uniform(25,39)
    t = round(t,2)
    h = random.uniform(50,95)
    h = round(h,2)
    return {'temperature':t, 'humidity':h}


def check_temperature():
    # temp = random_temperature()
    # humid = random_humidity()
    # temp, humid = random_mix()
    data = random_mix_dict()
    temp = data['temperature']
    humid = data['humidity']
    
    print('Temperature: {}'.format(temp))
    print('Humidity: {}%'.format(humid))

check_temperature()