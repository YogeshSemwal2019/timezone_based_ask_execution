# task_parser.py

from .task_def import Task

########################################################################
class TaskParser():
    
    @staticmethod
    def parse(taskstring):
        taskdetails = taskstring.split(" ")
        if len(taskdetails)>5:
            return Task(taskdetails[0],taskdetails[1],taskdetails[2],taskdetails[3],taskdetails[4],taskdetails[5])
        else:
            return Task(taskdetails[0],taskdetails[1],taskdetails[2],taskdetails[3],taskdetails[4])
            