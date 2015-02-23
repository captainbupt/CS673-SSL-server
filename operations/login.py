import json,log,constant

INFO_USERNAME = 'username'
INFO_PASSWORD = 'passwd'
RESULT_USERID = 'userid'
RESULT_NICKNAME = 'nickname'
RESULT_CREDIT = 'credit'
RESULT_RANK = 'rank'
RESULT_BALANCE = 'balance'

def verify(username, password):
	if not (isinstance(username,unicode) and isinstance(password,unicode)):
		return True
	return False

def getUserInfo(username):
	result = {}
	result[RESULT_USERID] = '0123456789'
	result[RESULT_NICKNAME] = 'Bob'
	result[RESULT_CREDIT] = 0
	result[RESULT_RANK] = 0
	result[RESULT_BALANCE] = [12.34]
	return result

def login(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	username = None
	password = None
	if INFO_USERNAME in data and INFO_PASSWORD in data:
		username = data[INFO_USERNAME]
		password = data[INFO_PASSWORD]
	else:
		log.warning('login: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(username, password):
		log.warning('login: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, getUserInfo(username)
	
