import _thread
import threading
import schedule
import time
from flask import flash
from app.models import User, Post
#from flask_login import current_user
#from flask import g, current_app
#from guess_language import guess_language
from app import db
from app import create_app
from app.email import send_email

""" 
    One of the most important things into this code is the conexion to the database inside the thread. For make that possible i worked with context. All can be understand with:
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/ 

    To understand the email configuration (and testing) I recommend read: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support/
"""
app = create_app()
def job(testInfo, name, current_user):
    
    print("recall contact fulanito", name)
    post = Post(body=testInfo, user_id=current_user, language = '')
    with app.app_context():
        send_email("test reminder", sender=app.config['ADMINS'][0], recipients=["the email that is going to get the reminders"], text_body="testing")
        db.session.add(post)
        db.session.commit()
        
    
def my_schedule_f(name, number, period, testInfo, current_user):
    
    """
        0 is to work with minutes and only for tests
        1 is to work with hours
        2 is to work with days
        3 is to work with weeks. But schedule don't have a option for this case so i use the one for "days" multiplicating the value of number for 7 (as there's 7 days in a week)
        4 is to work with months. We have the same situation that "3/weeks" and we apply the same logic to fixed, in this case we multiplicated number for 30 ( as there's 30 days in a month) 

        A example of how to "read" the instruction: "every x number of days do the job"
    """    
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
        schedule.every(0.1).minutes.do(job, testInfo=testInfo, name=name, current_user=current_user)
    while True:
        schedule.run_pending()
        time.sleep(1)

def thread_caller(name, number, period, testInfo, current_user):

    """ 
        Inside this function we have a thread, that make my_shedule_f work without forcing the rest of the web to stop.
        I put the thread inside a function so I could called from routes.py after it recieve the data from the form in add_reminder
    """
    current_user = current_user.id
    t1=threading.Thread(target=my_schedule_f, args=(name, number, period, testInfo, current_user))
    t1.start()
    

    
    