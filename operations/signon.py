import json,log,constant

INFO_USERNAME = 'username'
INFO_PASSWORD = 'passwd'
INFO_NICKNAME = 'nickname'
RESULT_USERID = 'userid'
RESULT_NICKNAME = 'nickname'
RESULT_CREDIT = 'credit'
RESULT_RANK = 'rank'
RESULT_RECORDS = 'records'
RESULT_BALANCE = 'balance'

def verify(username, password, nickname):
	if isinstance(username,str) and isinstance(password,str) and isinstance(nickname,str):
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

def signon(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	username = None
	password = None
	nickname = None
	if INFO_USERNAME in data:
		username = data[INFO_USERNAME]
	if INFO_PASSWORD in data:
		password = data[INFO_PASSWORD]
	if INFO_NICKNAME in data:
		nickname = data[INFO_NICKNAME]
	if username is None or password is None or nickname is None:
		log.warning('signon: missing username, password or nickname')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(username, password):
		log.warning('signon: unmatched username or password')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, getUserInfo(username)
	
