def is_valid(self, identifier):
	"""
	Return True if identifier is valid. In this base implementation, always return True.  (D)
	"""
	return True

class InvalidIdentifier(Exception):
	"""
	Exception raised if an identifier is not valid
	"""
	def __init__(self, identifier):
		self.identifier = identifier
	def __str__(self):
		return "Invalid identifier: '{}'".format(self.identifier)

class InvalidDataType(Exception):
	"""
	Exception raised if data type is not of correct type
	"""
	def __init__(self, data_type):
		self.data_type = data_type
	def __str__(self):
		return "Invalid data type: '{}'".format(self.data_type)

class InvalidParameter(Exception):
	"""
	Exception raised if the user has not provided any parameters
	"""
	def __init__(self):
		self.error = "Parameters are missing."
	def __str__(self):
		return self.error

class InvalidData(Exception):
	"""
	Exception raised if the data has not been valid
	"""
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return "Invalid data: '{}'".format(self.message)

class InvalidParameterSize(Exception):
	"""
	Exception raised if the user has provided an invalid parameter size
	"""
	def __init__(self, parameter_size):
		self.parameter_size = parameter_size
	def __str__(self):
		return "Invalid parameter size: '{}'".format(self.parameter_size)

class InvalidParameterType(Exception):
	"""
	Exception raised if the user has provided an invalid parameter type
	"""
	def __init__(self, parameter_type):
		self.parameter_type = parameter_type
	def __str__(self):
		return "Invalid parameter type: '{}'".format(self.parameter_type)

class InvalidParameterValue(Exception):
	"""
	Exception raised if the user has provided an invalid parameter value
	"""
	def __init__(self, parameter_value):
		self.parameter_value = parameter_value
	def __str__(self):
		return "Invalid parameter value: '{}'".format(self.parameter_value)

class InvalidDataValue(Exception):
	"""
	Exception raised if the user has provided an invalid data value
	"""
	def __init__(self, data_value):
		self.data_value = data_value
	def __str__(self):
		return "Invalid data value: '{}'".format(self.data_value)

class InvalidParameterValueSize(Exception):
	"""
	Exception raised if the user has provided an invalid parameter value size
	"""
	def __init__(self, parameter_size):
		self.parameter_size = parameter_size
	def __str__(self):
		return "Invalid parameter value size: '{}'".format(self.parameter_size)

class InvalidParameterType(Exception):
	"""
	Exception raised if the user has provided an invalid parameter type
	"""
	def __init__(self, parameter_type):
		self.parameter_type = parameter_type
	def __str__(self):
		return "Invalid parameter type: '{}'".format(self.parameter_type)

class InvalidParameterValueType(Exception):
	"""
	Exception raised if the user has provided an invalid parameter value type
	"""
	def __init__(self, parameter_type):
		self.parameter_type = parameter_type
	def __str__(self):
		return "Invalid parameter value type: '{}'".format(self.parameter_type)

class InvalidParameterCondition(Exception):
	"""
	Exception raised if the user has provided an invalid condition
	"""
	def __init__(self, condition):
		self.condition = condition
	def __str__(self):
		return "Invalid condition: '{}'".format(self.condition)

class InvalidParameterValueCondition(Exception):
	"""
	Exception raised if the user has provided an invalid condition
	"""
	def __init__(