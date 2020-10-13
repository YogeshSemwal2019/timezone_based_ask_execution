# task_execution.py

from datetime import datetime,timedelta
import calendar 

########################################################################
class TaskExecution():
    
    @staticmethod
    def execute(task_start_time,task_end_time,current_task_time,task,currentday=None):
        if task_start_time < datetime.strptime(current_task_time,"%H:%M:%S").time() or task_end_time < datetime.strptime(current_task_time,"%H:%M:%S").time() and currentday is not None: 
            if task.weekdays is not None:
               if currentday not in task.weekdays.split(","):
                   nextday = currentday
                   nextdate = datetime.now() + timedelta(days=1)                  
                   #print(str(nextday) + "  " + str(task_start_time) )                    
                   while nextday not in task.weekdays:
                       nextdate = nextdate + timedelta(days=1)
                       nextday = calendar.day_name[nextdate.weekday()]
                       #print(str(nextday) + "  " + str(task_start_time) )                       
                   return False,task_start_time,nextday
            return True                  
        elif task_start_time < datetime.strptime(current_task_time,"%H:%M:%S").time() and task_end_time > datetime.strptime(current_task_time,"%H:%M:%S").time(): 
            if task.weekdays is not None:
               #print(task.weekdays)
               if currentday not in task.weekdays:
                   nextday = currentday
                   nextdate = datetime.now() + timedelta(days=1)
                   while nextday not in task.weekdays:
                       nextdate = nextdate + timedelta(days=1)
                       nextday = calendar.day_name[nextdate.weekday()]
                   #print(str(nextday) + "  " + str(task_start_time) )                       
                   return False,task_start_time,nextday
            return True
        else:
            return False,task_start_time