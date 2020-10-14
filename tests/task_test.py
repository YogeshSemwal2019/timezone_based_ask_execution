# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:54:00 2020

@author:  yogesh.semwal
"""

import timezone_based_ask_execution
from datetime import datetime
from datetime import date
import calendar

def test_task_parse():
    task_input = "CALL U2 India 13:00:00 14:30:00"
    task = timezone_based_ask_execution.TaskParser.parse(task_input)
    assert task == timezone_based_ask_execution.Task("CALL","U2","India","13:00:00","14:30:00",None) 

def test_task_creation():
    task_input = "CALL U2 India 13:00:00 14:30:00"
    task = timezone_based_ask_execution.TaskParser.parse(task_input)
    current_task_time = timezone_based_ask_execution.TaskCreation(task).create_task_without_weekdays()  
    current_time = datetime.now().strftime("%H:%M:%S")
    print(str(current_time) + " " + str(current_task_time))
    assert current_time == current_task_time
 

def test_task_execution():
    task_input = "CALL U2 India 13:00:00 14:30:00"
    task = timezone_based_ask_execution.TaskParser.parse(task_input)
    task_start_time= datetime.strptime(task.start_time,"%H:%M:%S").time()
    task_end_time= datetime.strptime(task.end_time,"%H:%M:%S").time()    
    current_task_time = timezone_based_ask_execution.TaskCreation(task).create_task_without_weekdays()     
    result = timezone_based_ask_execution.TaskExecution.execute(task_start_time,task_end_time,current_task_time,task)
    if task_start_time < datetime.strptime(current_task_time,"%H:%M:%S") \
    .time() and task_end_time > datetime.strptime(current_task_time,"%H:%M:%S").time():
        assert result[0] == True
    else:
        assert result[0] == False

def test_task_runner():
    task_input = "CALL U2 India 13:00:00 14:30:00"    
    result = timezone_based_ask_execution.TaskController() \
    .task_runner_without_weekdays(task_input)
    print(result)
    assert result["status"] == "Success"

def test_task_runner_failed():
    task_input = "CALL U2 India test test"    
    result = timezone_based_ask_execution.TaskController() \
    .task_runner_without_weekdays(task_input)
    print("result " +str(result))
    assert result["status"] == "Failed"
    
def test_task_creation_weekdays():
    task_input = "CALL U2 India 13:00:00 14:30:00 Monday,Tuesday"
    task = timezone_based_ask_execution.TaskParser.parse(task_input)
    current_task_time,weekday = timezone_based_ask_execution. \
    TaskCreation(task).create_task_with_weekdays()  
    current_time = datetime.now().strftime("%H:%M:%S")
    current_day = calendar.day_name[date.today().weekday()] 
    print(str(current_time) + " " + str(current_task_time))
    print(str(weekday) + " " + str(current_day))    
    assert current_time == current_task_time and current_day==weekday
 
def test_task_runner_weekdays():
    task_input = "CALL U2 India 13:00:00 14:30:00 Monday,Tuesday"    
    result = timezone_based_ask_execution.TaskController() \
    .task_runner_with_weekdays(task_input)
    print(result)    
    assert result["status"] == "Success" 
    
def test_task_runner_weekdays_False():
    task_input = "CALL U2 India 13:00:00 14:30:00 Friday,Thursday"    
    result = timezone_based_ask_execution.TaskController() \
    .task_runner_with_weekdays(task_input)
    print(result)    
    assert result["status"] == "Success"  and result['result']== 'False'     

    