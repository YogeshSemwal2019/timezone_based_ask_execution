Problem Statement - Timezone based Task Execution

#Download project from git and setup using following command

python setup.py install

#copy config\config.ini to a location say F:\config\config.ini then create enviroment variable CONFIG_PATH

set CONFIG_PATH=F:\config

#then edit config.ini to set path of sqllite db say path=f:\task.db 

#then run nosetests as follows

nosetests tests

#Now run some examples for differen time zones

python example.py "CALL U2 India 13:00:00 14:30:00 Friday,Thursday"

#Current datetime:Wednesday  11:32:40
#Thursday 13:00:00


python example.py "CALL U2 Germany 19:08:00 20:30:00 Friday,Wednesday"

#Current datetime:Wednesday  08:03:21
#Wednesday 19:08:00

python example.py "CALL U2 Barbados 13:00:00 14:30:00"

#Current time:02:04:22
#13:00:00

python example.py "CALL U2 Barbados 13:00:00"

#Incorrect Input

#for libraries refer to requirements.txt

#Assumption is that user will not input current datetime and day

#timezones for each country is in countryinfo.py

#exmaple.py can be used to process inputs
#task_def creates task table in sqllite
#task_parser is responsible for parsing inputs
#task_creation  create the task and print current date and time
#task_execution executes task created and tells where it can be executed immediately or later
#task controller is controlling task creation, parser and execution and returning result to user
#tests/task_test.py has sample test cases which are executed on nosetest tests
