import core as c
import helpers as h
import transactions
import social

# if you append new columns, you need to ensure you have defined a handler for each of these in helpers.py
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
	listOfNewSocialInteractions = ""

	# if asked for headers, first we print out the core headers, followed by the extra ones
	if headers:
		#core columns
		for idx, item in enumerate(c.coreColumns):
			listOfNewRows += c.quote + item + c.quote
			if idx+1 != len(c.coreColumns):
				listOfNewRows += c.comma
		#extra columns
		if len(extraColumns) > 0:
			listOfNewRows += c.comma
		for idx, item in enumerate(extraColumns):
			listOfNewRows +=c.quote + item + c.quote
			if idx+1 != len(extraColumns):
				listOfNewRows += c.comma
		listOfNewRows += c.newline

	# if asked for transactions (related child records) we print out their headers for transactions and social media interactions
	if buildtransactions & headers:
		for idx, item in enumerate(transactions.columnData):
			listOfNewTransactions += c.quote + item + c.quote
			if idx+1 != len(transactions.columnData):
				listOfNewTransactions += c.comma
		listOfNewTransactions += c.newline

		listOfNewSocialInteractions += c.quote + "customer_id" + c.quote + c.quotecomma + "email" + c.quotecomma		
		for idx, item in enumerate(social.columnData):
			listOfNewSocialInteractions += c.quote + item + c.quote
			if idx+1 != len(transactions.columnData):
				listOfNewSocialInteractions += c.comma
		listOfNewSocialInteractions += c.newline		

	# start of main iter
	rowcount = 0
	for newrow in range(rows):
		newrow = ""
		identity_bundle = c.handlerMap("identity_bundle")
		geolocation_bundle = c.handlerMap("geolocation_bundle")
		newid = c.handlerMap("customer_id")
		birthdate = str(c.handlerMap("birth_dt"))

		# 1 the ID
		newrow+= c.quote + newid + c.quotecomma								
		# 2 the identity info
		for item in range(len(identity_bundle)):						
			newrow+= c.quote + identity_bundle[item] + c.quotecomma
		# 3 the geo info
		for item in range(len(geolocation_bundle)):						
			newrow+= c.quote + geolocation_bundle[item] + c.quotecomma
		# 4 birthdate
		newrow+= c.quote + birthdate + c.quotecomma							
		# 5 any extra columns you have defined
		for idx, item in enumerate(extraColumns):					
			newrow += c.quote + h.extraHandlerMap(item) + c.quote
			newrow += c.comma if idx+1 != len(extraColumns) else ""
		#6 newline if not last line
		if rowcount != rows:														
			newrow+= c.newline
		
		listOfNewRows+= newrow

		# if transactions were requested, we do that here
		if buildtransactions:
			maxrows = int(args[0])
			listOfNewTransactions += transactions.generateTransactions(newid, maxrows)
			listOfNewSocialInteractions += social.generateSocialInteractions(newid, maxrows, identity_bundle[4])

		rowcount+=1

	return listOfNewRows, listOfNewTransactions, listOfNewSocialInteractions
