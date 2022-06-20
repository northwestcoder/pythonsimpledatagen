# for this example, you will need to pip install flask
# and/or read the docs on flask: https://palletsprojects.com/p/flask/
#
# this example provides a payload URL for fake data
#
# from this directory, you would start flask from the command line like so:
#   $export FLASK_APP=flaskserver.py
#   $flask run
#
# it will then say
# "Running on http://127.0.0.1:5000/"
# 
# and if you go to 
# http://127.0.0.1:5000/dynamic
# http://127.0.0.1:5000/static
# you should see 1,000 lines of randomly generated data (the random one will change on each refresh)

from flask import Flask

import people

app = Flask(__name__)

args = (True, 1000, True, 10)

static = people.createData(*args)

# this next route generates a var each time the route is called
@app.route('/dynamicpeople')
def randomPayload():

	payload = people.createData(headers=True, rows=1000, buildtransactions=False)
	return payload[0]


# this one uses 'staticdata' created outside of the route, 
# so it will remain stable for the lifetime of the flask invocation
@app.route('/staticpeople')
def staticPayload():

	return static[0]

@app.route('/statictransactions')
def staticPayloadTransactions():

	return static[1]

@app.route('/staticsocial')
def staticPayloadSocial():

	return static[2]	