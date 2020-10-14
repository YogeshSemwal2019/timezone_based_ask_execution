# task_execution.py

from datetime import datetime,timedelta
import calendar 
import pytz 

########################################################################
class TaskExecution():

    @staticmethod
    def getnextday(taskweekdays,task,task_start_time,currentday,current_task_time):
        if taskweekdays is not None:
           if currentday not in taskweekdays.split(","):
               nextday = currentday
               nextdate = datetime.now( pytz.timezone(task.timezone))                 
               #print(str(nextday) + "  " + str(task_start_time) )                    
               while nextday not in taskweekdays.split(","):
                   nextdate = nextdate + timedelta(days=1)
                   nextday = calendar.day_name[nextdate.weekday()]                      
               return False,task_start_time,nextday  
           elif task_start_time > datetime.strptime \
           (current_task_time,"%H:%M:%S").time():
               return False,task_start_time,currentday  
        return True,
    
    @staticmethod
    def execute(task_start_time,task_end_time,current_task_time,task,currentday=None):
        if (task_start_time > datetime.strptime(current_task_time,"%H:%M:%S").time() or\
        task_end_time < datetime.strptime \
        (current_task_time,"%H:%M:%S").time()) \
        and currentday is not None: 
            return TaskExecution.getnextday(task.weekdays,task,task_start_time,\
            currentday,current_task_time)                  
        elif task_start_time < datetime.strptime(current_task_time,"%H:%M:%S").time()\
        and task_end_time > datetime.strptime(current_task_time,"%H:%M:%S").time() : 
            return TaskExecution.getnextday(task.weekdays,task,task_start_time,\
            currentday,current_task_time)   
        else:
            return False,task_start_time