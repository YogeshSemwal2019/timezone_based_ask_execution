# task_creation.py

from .config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from datetime import date
import calendar

########################################################################
class TaskCreation():
    task = None
    #----------------------------------------------------------------------
    def __init__(self, task):
        """"""
        self.task = task
        self.engine = create_engine('sqlite:///' + config.get('database','path'), echo=False)     
    
    def create_task_without_weekdays(self):        
        # create a Session
        Session = sessionmaker(bind=self.engine)
        session = Session()
        
        # Add the record to the session object
        session.add(self.task)
        # commit the record the database
        session.commit()  
        
        current_time = datetime.now().strftime("%H:%M:%S")
        
        print("Current time:" + str(current_time) )
        
        return current_time
        
    def create_task_with_weekdays(self):        
        current_time = self.create_task_without_weekdays()
        current_day = calendar.day_name[date.today().weekday()] 

        print("Current datetime:" + str(current_day) + "  " + str(current_time) )
        
        return current_time,current_day
        
        