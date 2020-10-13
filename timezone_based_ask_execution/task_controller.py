# task_controller.py

from datetime import datetime
from .task_def import Task
from .task_creation import TaskCreation
from .task_execution import TaskExecution
from .task_parser import TaskParser

########################################################################
class TaskController(object):    
    tsk_creation = TaskCreation
    tsk_execution = TaskExecution
    tsk_parser = TaskParser
    
            
    @classmethod
    def task_runner_without_weekdays(self,task_input):
        try:
            task = self.tsk_parser.parse(task_input)
            task_start_time= datetime.strptime(task.start_time,"%H:%M:%S").time()
            task_end_time= datetime.strptime(task.end_time,"%H:%M:%S").time()               
            current_task_time = self.tsk_creation(task).create_task_without_weekdays()     
            result = self.tsk_execution.execute(task_start_time,task_end_time,current_task_time,task)            
            if type(result[0]) == bool:
                if result[0] == True:
                    return {"result":str(result[0]), "status":"Success" } 
                else:
                    return {"result":str(result[0]), "status":"Success",  "nextexecution": result[1].strftime("%H:%M:%S") }
            else:
               return {"result":str(result[0]), "status":"Failed"}  
        except Exception as e:
            return {"result":str(e), "status":"Failed"} 

            
        
    @classmethod
    def task_runner_with_weekdays(self,task_input):
        try:
            task = self.tsk_parser.parse(task_input)
            task_start_time= datetime.strptime(task.start_time,"%H:%M:%S").time()
            task_end_time= datetime.strptime(task.end_time,"%H:%M:%S").time()                   
            current_task_time,currentday = self.tsk_creation(task).create_task_with_weekdays()     
            result = self.tsk_execution.execute(task_start_time,task_end_time,current_task_time,task,currentday)            
            if type(result[0]) == bool:
                if result[0] == True:
                    return {"result":str(result[0]), "status":"Success" } 
                else:
                    if len(result)>2:
                        return {"result":str(result[0]), "status":"Success",  "nextexecution": (result[2] + " " + result[1].strftime("%H:%M:%S")) }
                    else:
                        return {"result":str(result[0]), "status":"Success",  "nextexecution": result[1].strftime("%H:%M:%S") }  
            else:
               return {"result":str(result[0]), "status":"Failed"}  
        except Exception as e:
            return {"result":str(e), "status":"Failed"} 
   