class CallDetail():
	def __init__(self, caller, called, duration, callType):
		self.caller = caller
		self.called = called
		self.duration = duration
		self.callType = callType

class Util:
	
	def __init__(self):
		self.list_of_call_object = None
	
	def parse_customer(self, list_of_call_string):
		self.list_of_call_object = []
		for call in list_of_call_string:
			detail = call.split(',')
			#appending the objects of CallDetail class to list_of_call_object
			self.list_of_call_object.append(CallDetail(detail[0], detail[1], detail[2], detail[3]))
	
	def print_call_detail(self):
		for call in self.list_of_call_object:
			print("Caller:"+call.caller+"\nCalled:"+call.called+"\nDuration:"+call.duration+"\nType:"+call.callType+"\n")
	
if __name__ == "__main__":
	call1 = '9990000000,9330875431,23,STD'
	call2 = '9374659023,9382612839,25,ISD'
	call3 = '8765432198,4561932789,30,LOCAL'
	list_of_call_string = [call1, call2, call3]
	util = Util()
	util.parse_customer(list_of_call_string)
	util.print_call_detail()
