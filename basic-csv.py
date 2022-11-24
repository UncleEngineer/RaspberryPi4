import csv

def writetocsv(data):
    # data = [25.66,50.66]
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)



writetocsv([20,55])


