from cimpy.cgmes_v2_4_15.Limit import Limit


class AccumulatorLimit(Limit):
	'''
	Limit values for Accumulator measurements.

	:value: The value to supervise against. The value is positive. Default: 
	:LimitSet: The limit values used for supervision of Measurements. Default: 
		'''

	cgmesProfile = Limit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						'LimitSet': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Limit: \n' + Limit.__doc__ 

	def __init__(self, value = , LimitSet = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.value = value
		self.LimitSet = LimitSet
		
	def __str__(self):
		str = 'class=AccumulatorLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
