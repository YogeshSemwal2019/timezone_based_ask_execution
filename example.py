# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:40:34 2020

@author: yogesh.semwal
"""

import timezone_based_ask_execution
import sys

if __name__ == "__main__":
    task_input = sys.argv[1]    
    if len(task_input.split(" "))<5:
        print("Incorrect Input")  
    elif len(task_input.split(" "))>5:
        result = timezone_based_ask_execution.TaskController().task_runner_with_weekdays(task_input)
        if result['result'] == 'True':
            print(result['result'])   
        else:
            print(result['nextexecution'])
    else:
        result = timezone_based_ask_execution.TaskController().task_runner_without_weekdays(task_input)
        if result['result'] == 'True':
            print(result['result'])   
        else:
            print(result['nextexecution'])      