from cimpy.output.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindGenType4IEC(WindTurbineType3or4IEC):
	'''
	IEC Type 4 generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.4.

	:dipmax: Maximum active current ramp rate (di). It is project dependent parameter. Default: 
	:diqmin: Minimum reactive current ramp rate (d). It is case dependent parameter. Default: 
	:diqmax: Maximum reactive current ramp rate (di). It is project dependent parameter. Default: 
	:tg: Time constant (T). It is type dependent parameter. Default: 
		'''

	cgmesProfile = WindTurbineType3or4IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dipmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'diqmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'diqmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4IEC: \n' + WindTurbineType3or4IEC.__doc__ 

	def __init__(self, dipmax = , diqmin = , diqmax = , tg = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dipmax = dipmax
		self.diqmin = diqmin
		self.diqmax = diqmax
		self.tg = tg
		
	def __str__(self):
		str = 'class=WindGenType4IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
