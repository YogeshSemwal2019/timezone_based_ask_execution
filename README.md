Problem Statement - Timezone based Task Execution

python setup.py install

#copye config\config.ini to a location say F:\config\config.ini then create enviroment variable CONFIG_PATH

set CONFIG_PATH=F:\config

#then edit config.in to set path of sqllite db say path=f:\task.db 

nosetests tests

python example.py "CALL U2 India 13:00:00 14:30:00 Friday,Thursday"
