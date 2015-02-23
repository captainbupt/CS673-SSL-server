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
	if not (isinstance(username,unicode) and isinstance(password,unicode) \
		and isinstance(nickname,unicode)):
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
	if INFO_USERNAME in data and INFO_PASSWORD in data and INFO_NICKNAME in data:
		username = data[INFO_USERNAME]
		password = data[INFO_PASSWORD]
		nickname = data[INFO_NICKNAME]
	else:
		log.warning('signon: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(username, password):
		log.warning('signon: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, getUserInfo(username)
	
