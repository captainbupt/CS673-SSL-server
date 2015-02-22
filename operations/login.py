import json,log,constant

INFO_USERNAME = 'username'
INFO_PASSWORD = 'passwd'
RESULT_USERID = 'userid'
RESULT_NICKNAME = 'nickname'
RESULT_CREDIT = 'credit'
RESULT_RANK = 'rank'
RESULT_RECORDS = 'records'
RESULT_BALANCE = 'balance'

def verify(username, password):
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
		log.warning('missing username or password')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(username, password):
		log.warning('unmatched username or password')
		statu = constant.STATUS_INFORMATION_UNMATCHED
		return statu,result
	return statu, getUserInfo(username)
	