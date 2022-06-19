import string
import random
import os

import inputs

extrahandlers = {
"account_type" : "AccountHandler",
"phone_number" : "PhoneHandler",
"job_type" : "JobTypeHandler",
"cc_number" : "CCNumberHandler",
"ssn" : "SsnHandler",
"allergies" : "AllergyHandler",
"blood_type" : "BloodTypeHandler",
"last_ipaddress" : "IPAddressHandler"
}

def AccountHandler():
	return random.choice(inputs.df_account_types)

def PhoneHandler():
	return random.choice(inputs.df_phones)

def JobTypeHandler():
	return random.choice(inputs.df_jobs)

def SsnHandler():
	return str(random.randint(100,999)) + "-" + str(random.randint(1,99)) + "-" + str(random.randint(1000,9999))

def AllergyHandler():
	return random.choice(inputs.df_allergies)

def BloodTypeHandler():
	return random.choice(inputs.df_bloodtypes)

def IPAddressHandler():
	return random.choice(inputs.df_ip_addresses)

# our handler map
def extraHandlerMap(type):
	return globals()[extrahandlers.get(type)]()

