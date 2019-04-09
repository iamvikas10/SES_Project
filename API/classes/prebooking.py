class Prebooking:
	def __init__(self):
		self.__slotNo = None;
		self.__ExpectedArrival = None;
		self.__rcNo = None;
		self.__ExactArrival = None;
		self.__bookingStatus = None;
		self.__phoneNo = None;
		self.__AreaId = None;

	def get_slotNo(self):
		return self.__slotNo;
	def set_slotNo(self, value):
		self.__slotNo= value;

	def get_ExpectedArrival(self):
		return self.__ExpectedArrival
	def set_ExpectedArrival(self, value):
		self.__ExpectedArrival = value;

	def get_rcNo(self):
		return self.__rcNo;
	def set_rcNo(self, value):
		self.__rcNo = value;

	def get_phoneNo(self):
		return self.__phoneNo;
	def set_phoneNo(self, value):
		self.__phoneNo = value;


	def get_ExactArrival(self):
		return self.__ExactArrival
	def set_ExactArrival(self, value):
		self.__ExactArrival = value;

	def get_bookingStatus(self):
		return self.__bookingStatus
	def set_bookingStatus(self, value):
		self.__bookingStatus = value;

	def get_AreaId(self):
		return self.__AreaId
	def set_AreaId(self, value):
		self.__AreaId = value;

