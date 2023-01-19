import time
import threading

def Shower():
    for i in range(10):
        print('กำลังอาบน้ำ',i)
        time.sleep(0.5)

def Toothbrush():
    for i in range(10):
        print('กำลังแปรงฟัน',i)
        time.sleep(0.2)


task1 = threading.Thread(target=Toothbrush)
task2 = threading.Thread(target=Shower)

t1 = time.time()
task1.start()
task2.start()

task1.join()
task2.join()
#Toothbrush()
#Shower()
t2 = time.time()
print('Time:',t2-t1)

