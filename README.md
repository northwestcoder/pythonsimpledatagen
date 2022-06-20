## simpledatagen - lightweight data generator for various uses

##### This app builds three files - people.csv, transactions.csv and social.csv - with a customer primary key between them. The premise is that you would then load this data into your favorite database or data science tool.

- There are text inputs for various random data generation, in the './inputs' directory.

- We've tried to eliminate all possible 3rd party modules. Why? Because it's fun :) these examples should work on pretty much any version of python and run with only:
```
import random
import datetime
import time
import string
import os
```

... as well as any custom imports from this same project.

### gendata.py
```
your_cli_prompt>>$python3 gendata.py
```

- Generates 1000 customers and each customer gets 1-10 transactions with a relational key, and outputs two CSV files to this same directory. 
- Change the args as you see fit:

```
# args: (csv headers?, how many rows?, create transactions?, max trans per person?)
args = (True, 1000, True, 10)
```

### flask.py

- Using *Flask* (you will need to _pip install flask_ in your python environment), we create a few simple endpoints which will generate 1,000 lines of fake people data by calling people.py, this area is left as an exercise for the reader. 

*Enjoy!*