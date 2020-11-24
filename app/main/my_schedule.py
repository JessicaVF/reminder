import _thread
import threading
import schedule
import time
from flask import flash
from app.models import User, Post
from flask_login import current_user


def job(name ):
    print("recall contact", name)
    
    """post = Post(body=posti, author=current_user, language='')
    db.session.add(post)
    db.session.commit()"""
    

def my_schedule_f(name, number, period):
    
    """
    0 is to work with minutes and only for tests
    1 is to work with hours
    2 is to work with days
    3 is to work with weeks. But schedule don't have a option for this case so i use the one for "days" multiplicating the value of number for 7 (as there's 7 days in a week)
    4 is to work with months. We have the same situation that "3/weeks" and we apply the same logic to fixed, in this case we multiplicated number for 30 ( as there's 30 days in a month) 

    A example of how to "read" the instruction: "every x number of days do the next task/job"
    """
    print("into the fuction")

    if period == "1":
        schedule.every(number).hours.do(job, name=name)
    elif period == "2":
        schedule.every(number).day.do(job, name=name)
    
    elif period == "3":
        number = number * 7
        schedule.every(number).day.do(job, name=name)
    elif period == "4":
        number = number * 30
        schedule.every(number).day.do(job, name=name)
    elif period == "0":
        print("into the elif")
        schedule.every(0.1).minutes.do(job, name=name)
        print("after the elif")
    while True:
        schedule.run_pending()
        time.sleep(1)

def thread_caller(name, number, period):

    """ 
    The prints in this code are just for testing reasons and don't clash with the final user experience:

    Inside this function we have a thread, that make my_shedule_f work without forcing the rest of the web to stop.
    I put the thread inside a function so I could called from routes.py after it recieve the data from the form in add_reminder

    The t1.join() is commented because it was blocking a (single) message flash() and it looks like the absent of t1.join() don't affect anything negatively. I let it here just in case I need it in the future or in
    case I realize is actuqlly need it

    """

    print("the thread was activated")
    t1=threading.Thread(target=my_schedule_f, args=(name, number,period))
    t1.start()
    """t1.join()"""
    
    print("the thread ended")  
