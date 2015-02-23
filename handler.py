import json, log, constant
from operations import *

operations={'login':login,'signon':signon,'recharge':recharge,'tranhistory':tranhistory,\
'recordhistory':recordhistory}

def handle_data(data_str):
	response = {constant.PARAMETER_STATUS:constant.STATUS_SUCCESS,constant.PARAMETER_RESULT:{}}
	data =None
	try:
		data = json.loads(data_str)
	except 	ValueError:
		response[constant.PARAMETER_STATUS]=constant.STATUS_JSON_UNMATCHED
		log.warning('handler: receive none json data')
	if data is not None:
		opt = data[constant.PARAMETER_OPERATION]
		if isinstance(opt,unicode) and opt in operations:
			status,result = operations[opt](data[constant.PARAMETER_INFORMATION])
			response[constant.PARAMETER_STATUS] = status
			response[constant.PARAMETER_RESULT] = result
		else:
			response[constant.PARAMETER_STATUS]=constant.STATUS_OPERATION_UNSUPPORTED
			log.warning('handler: receive unsupported request')
	return json.dumps(response)

#print handle_data('{"opt":"login","info":{"passwd":"0A987B5CD87B5BBC","username":"bob123"}}')

#print handle_data('{"opt":"tranhistory","info":{"userid":"0000000001","page":1,"num":10}}')
print handle_data('{"opt":"recordhistory","info":{"userid":"0000000001","page":1,"num":10}}')