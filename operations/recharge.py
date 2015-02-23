import json,log,constant

INFO_USERID = 'userid'
INFO_CARDNUMBER = 'number'
INFO_EXPIRE = 'expire'
INFO_SN = 'securitynumber'
INFO_AMOUNT = 'amount'

def verify(userid, number, expire, securitynumber, amount):
	if not (isinstance(userid,unicode) and isinstance(number,unicode) \
	and isinstance(expire,unicode) and isinstance(securitynumber,unicode) and isinstance(amount,float)):
		return False
	return True

def addAmount(userid,amount):
	return True

def recharge(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	userid = None
	cardnumber = None
	expire = None
	sn = None
	amount = None
	if INFO_USERID in data and INFO_CARDNUMBER in data\
	and INFO_EXPIRE in data and INFO_SN in data and INFO_AMOUNT in data:
		userid = data[INFO_USERID]
		cardnumber = data[INFO_CARDNUMBER]
		expire = data[INFO_EXPIRE]
		sn = data[INFO_SN]
		amount = data[INFO_AMOUNT]
	else:
		log.warning('recharge: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(userid, number, expire, securitynumber, amount):
		log.warning('recharge: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, result
	
