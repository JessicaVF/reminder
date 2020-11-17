import schedule
import time

def job(name):
    print("recall contact",name)

def my_schedule_f(name, number, period):

    if period == "1":
        schedule.every(number).day.do(job, name=name)
    elif period == "2":
        schedule.every(number).hour.do(job, name=name)
    #por ahora para acceder a minute debo seleccionar weeks
    elif period == "3":
        schedule.every().minute.at(":10").do(job, name=name)
        
    while True:
        schedule.run_pending()
        time.sleep(1)