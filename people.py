import core
import helpers
import transactions

quote				= "\""
quotecomma			= "\","
comma				= ","
newline				= "\n"

# if you append new columns, you need to ensure you have defined a handler for these in helpers.py
# we have provided a few as examples

extraColumns = [ 
"job_type",
"account_type",
"phone_number",
"ssn",
"allergies",
"blood_type",
"last_ipaddress"
]

def createData(headers: bool, rows: int, buildtransactions: bool, *args) -> str:

	listOfNewRows = ""
	listOfNewTransactions = ""

	# if asked for headers, first we print out the core headers, followed by the extra ones
	if headers:
		for idx, item in enumerate(core.coreColumns):
			listOfNewRows += quote + item + quote
			if idx+1 != len(core.coreColumns):
				listOfNewRows += comma
	
		if len(extraColumns) > 0:
			listOfNewRows += comma
		for idx, item in enumerate(extraColumns):
			listOfNewRows +=quote + item + quote
			if idx+1 != len(extraColumns):
				listOfNewRows += comma

		listOfNewRows += newline

	# if asked for transactions (child records) we print out their headers
	if buildtransactions & headers:
		for idx, item in enumerate(transactions.columnData):
			listOfNewTransactions += quote + item + quote
			if idx+1 != len(transactions.columnData):
				listOfNewTransactions += comma
		listOfNewTransactions += newline		

	# start of main iter
	rowcount = 0
	for newrow in range(rows):
		newrow = ""
		identity_bundle = core.handlerMap("identity_bundle")
		geolocation_bundle = core.handlerMap("geolocation_bundle")
		newid = core.handlerMap("customer_id")
		birthdate = str(core.handlerMap("birth_dt"))

		# 1 the ID
		newrow+= quote + newid + quotecomma								
		# 2 the identity info
		for item in range(len(identity_bundle)):						
			newrow+= quote + identity_bundle[item] + quotecomma
		# 3 the geo info
		for item in range(len(geolocation_bundle)):						
			newrow+= quote + geolocation_bundle[item] + quotecomma
		# 4 birthdate
		newrow+= quote + birthdate + quotecomma							
		# 5 any extra columns you have defined
		for idx, item in enumerate(extraColumns):					
			newrow += quote + helpers.extraHandlerMap(item) + quote
			newrow += comma if idx+1 != len(extraColumns) else ""
		#6 newline if not last line
		if rowcount != rows:														
			newrow+= newline
		
		listOfNewRows+= newrow

		# if transactions were requested, we do that here
		if buildtransactions:
			maxrows = int(args[0])
			listOfNewTransactions += transactions.generateTransactions(newid, maxrows)

		rowcount+=1

	return listOfNewRows, listOfNewTransactions
