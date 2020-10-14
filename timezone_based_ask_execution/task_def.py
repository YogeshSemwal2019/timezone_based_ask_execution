# task_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from .config import config
from .countryinfo import gettimezone 
from datetime import datetime

engine = create_engine('sqlite:///' + config.get('database','path'), echo=False)
Base = declarative_base()

########################################################################
class Task(Base):
    
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task_type = Column(String)
    user = Column(String)
    country = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    timezone = Column(String)
    weekdays = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, task_type, user, country, start_time,end_time,weekdays=None):

        self.task_type = task_type
        self.user = user
        self.timezone = gettimezone(country)        
        self.country = country
        self.start_time = start_time
        self.end_time = end_time
        self.weekdays = weekdays

    def __eq__(self, other): 
        if not isinstance(other, Task):
            # don't attempt to compare against unrelated types
            return NotImplemented

        condition1= self.task_type == other.task_type
        condition2= condition1 and self.user == other.user
        condition3= condition2 and self.country == other.country
        condition4= condition3 and self.start_time == other.start_time
        condition5= condition4 and self.end_time == other.end_time
        condition6= condition5 and self.timezone == other.timezone
        condition7= condition6 and self.weekdays == other.weekdays
        
        return condition7 
    
# create tables
Base.metadata.create_all(engine)