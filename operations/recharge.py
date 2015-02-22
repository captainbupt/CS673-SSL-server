import json,log,constant

INFO_USERID = 'userid'
INFO_CARDNUMBER = 'number'
INFO_EXPIRE = 'expire'
INFO_SN = 'securitynumber'
INFO_AMOUNT = 'amount'

def verify(username, password):
	if isinstance(username,str) and isinstance(password,str):
		return False
	return True

def getUserInfo(username):
	result = {}
	result[RESULT_USERID] = '0123456789'
	result[RESULT_NICKNAME] = 'Bob'
	result[RESULT_CREDIT] = 0
	result[RESULT_RANK] = 0
	result[RESULT_RECORDS] = ['0000000001','0000000002']
	result[RESULT_BALANCE] = [12.34]
	return result

def login(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	username = None
	password = None
	if INFO_USERNAME in data:
		username = data[INFO_USERNAME]
	if INFO_PASSWORD in data:
		password = data[INFO_PASSWORD]
	if username is None or password is None:
		log.warning('login: missing username or password')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(username, password):
		log.warning('login: unmatched username or password')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, getUserInfo(username)
	
