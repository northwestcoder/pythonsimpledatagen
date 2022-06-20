import random
import datetime 

import core
import helpers

quote 			= "\""
quotecomma 		= "\","
comma 			= ","
newline 		= "\n"

columnData = [
'social_last_uri',
'social_timestamp',
'social_ip',
'social_sha256',
'social_uuid4'
]

def generateSocialInteractions(customerid: str, maxinteractions: int, email: str):

	rowcount = 0
	social = ""

	for newrow in range(random.randint(1,maxinteractions)):   # for each customer we gen 1-N social interactions, change as desired
		newrow = ""
		newrow += quote + customerid + quotecomma
		newrow += quote + email + quotecomma

		for idx, item in enumerate(columnData):					
			newrow += quote + helpers.extraHandlerMap(item) + quote
			newrow += comma if idx+1 != len(columnData) else ""
		#6 newline if not last line
		if rowcount != maxinteractions:														
			newrow+= newline
		
		social += newrow

		rowcount+=1

	return(social)