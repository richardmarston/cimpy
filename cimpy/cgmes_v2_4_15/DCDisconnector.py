from cimpy.output.DCSwitch import DCSwitch


class DCDisconnector(DCSwitch):
	'''
	A disconnector within a DC system.

		'''

	cgmesProfile = DCSwitch.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DCSwitch: \n' + DCSwitch.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=DCDisconnector\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
