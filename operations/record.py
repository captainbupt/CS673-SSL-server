import json,log,constant, time

INFO_USERID = 'userid'
INFO_PAGE = 'page'
INFO_NUM = 'num'
RESULT_HISTORYIES = 'histories'
RESULT_TIME = 'time'
RESULT_ID = 'transactionid'
RESULT_WINNING = 'winning'
RESULT_TYPE = 'type'

def getHistory(userid, page, num):
	histories = []
	for i in range((page-1)*num, page*num):
		result = {}
		result[RESULT_TIME] = time.time()*1000
		result[RESULT_ID] = '%010d'%((page-1)*num+i)
		result[RESULT_WINNING] = i%2
		result[RESULT_TYPE] = 1
		histories.append(result)
	return {RESULT_HISTORYIES:histories}

def verify(userid, page, num):
	if not (isinstance(userid,unicode) and isinstance(page,int) \
	and isinstance(num,int)):
		return False
	return True

def recordhistory(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	userid = None
	page = None
	num = None
	if INFO_USERID in data and INFO_PAGE in data\
	and INFO_NUM in data :
		userid = data[INFO_USERID]
		page = data[INFO_PAGE]
		num = data[INFO_NUM]
	else:
		log.warning('transaction: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(userid, page, num):
		log.warning('transaction: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, getHistory(userid, page, num)
	
