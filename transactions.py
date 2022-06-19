import random
import datetime 

import core
import helpers

quote 			= "\""
quotecomma 		= "\","
comma 			= ","
newline 		= "\n"

columnData = [
'customer_id',
'orderid',
'purchasedatetime',
'transactiontotal',
'numberofitems',
'productcode',
'productcategory',
'cc_number']


#let's define a 'recent' date range going back a max of 1800 days
trans_start_date = datetime.date.today() - datetime.timedelta(days=1800)
trans_end_date = datetime.date.today() - datetime.timedelta(days=1)
time_between_dates = trans_end_date - trans_start_date
trans_days_between_dates = time_between_dates.days

def generateTransactions(customerid: str, maxtrans: int):

	rowcount = 0
	transactions = ""

	for newrow in range(random.randint(1,maxtrans)):   # for each customer we gen 1-N transactions, change as desired
		newrow = ""
		transtotal = round(random.triangular(100, 2000),2) # triangular is awesome and creates a nice normal distro of values
		numitems = random.randint(1,15)

		newrow += quote + customerid + quotecomma
		newrow += quote + core.coreNextCustomerID() + quotecomma

		random_number_of_days = random.randrange(trans_days_between_dates)
		random_date = trans_start_date + datetime.timedelta(days=random_number_of_days)		
		newrow += quote + str(random_date) + quotecomma
		newrow += quote + str(transtotal) + quotecomma
		newrow += quote + str(numitems) + quotecomma		

		prodcode = random.randint(700000000,900000000)

		#product codes
		newrow += quote + str(prodcode) + quotecomma		
		newrow += quote + ("PR" + str(prodcode)[:3]) + quotecomma

		# CC number
		newrow += quote + str(random.randint(1000,9999)) + " "  \
						+ str(random.randint(1000,9999)) + " "  \
						+ str(random.randint(1000,9999)) + " "  \
						+ str(random.randint(1000,9999)) + quote

		if rowcount != maxtrans:			
			newrow += newline

		transactions += newrow
		rowcount+=1

	return(transactions)
