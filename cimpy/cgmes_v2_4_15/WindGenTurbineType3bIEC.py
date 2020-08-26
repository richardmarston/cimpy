from cimpy.output.WindGenTurbineType3IEC import WindGenTurbineType3IEC


class WindGenTurbineType3bIEC(WindGenTurbineType3IEC):
	'''
	IEC Type 3B generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.3.

	:fducw: Crowbar duration versus voltage variation look-up table (f()). It is case dependent parameter. Default: 
	:tg: Current generation Time constant (). It is type dependent parameter. Default: 
	:two: Time constant for crowbar washout filter (). It is case dependent parameter. Default: 
	:mwtcwp: Crowbar control mode ().   The parameter is case dependent parameter. Default: 
	:xs: Electromagnetic transient reactance (x). It is type dependent parameter. Default: 
		'''

	cgmesProfile = WindGenTurbineType3IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'fducw': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'two': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwtcwp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xs': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindGenTurbineType3IEC: \n' + WindGenTurbineType3IEC.__doc__ 

	def __init__(self, fducw = , tg = , two = , mwtcwp = , xs = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.fducw = fducw
		self.tg = tg
		self.two = two
		self.mwtcwp = mwtcwp
		self.xs = xs
		
	def __str__(self):
		str = 'class=WindGenTurbineType3bIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
