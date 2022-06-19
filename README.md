## simpledatagen - lightweight data generator for various uses

##### This app builds two files - people.csv and transactions.csv - with a customer primary key between them. The premise is that you would then load this data into your favorite database or data science tool.

- There are text inputs for various random data generation, in the './inputs' directory.

- We've tried to eliminate all possible 3rd party modules. Why? Because it's fun. These examples run with only:
	- import random
	- import datetime
	- import time
	- import string
	- import os
	- as well as custom imports from this same directory

### gendata.py

- Main caller for command line purposes. 
- Generates 1000 customers and each customer gets 1-10 transactions with a relational key, and outputs two CSV files to this same directory. 
- Change the args as you see fit:
```
# args: (csv headers?, how many rows?, create transactions?, max transactions per person?)
args = (True, 1000, True, 10)
```

### flaskserver.py

- Using *Flask* (you will need to _pip install flask_ in your python environment), we create two simple endpoints "/static" and "/dynamic" - which will both autogenerate 1,000 lines of fake people data by calling gendata. 
- For the static endpoint, the data is generated once per lifetime of the flask run. 
- For the dynamic endpoint, each browser refresh to the endpoint will regen the data.
- Read the comments in this file for more info and run instructions.