from cimpy.output.IdentifiedObject import IdentifiedObject


class WindContCurrLimIEC(IdentifiedObject):
	'''
	Current limitation model.  The current limitation model combines the physical limits.  Reference: IEC Standard 61400-27-1 Section 6.6.5.7.

	:imax: Maximum continuous current at the wind turbine terminals (). It is type dependent parameter. Default: 
	:imaxdip: Maximum current during voltage dip at the wind turbine terminals (). It is project dependent parameter. Default: 
	:mdfslim: Limitation of type 3 stator current  ():  - false=0: total current limitation,  - true=1: stator current limitation).  It is type dependent parameter. Default: 
	:mqpri: Prioritisation of q control during LVRT (): - true = 1: reactive power priority, - false = 0: active power priority.  It is project dependent parameter. Default: 
	:tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 
	:WindTurbineType3or4IEC: Wind turbine type 3 or 4 model with which this wind control current limitation model is associated. Default: 
	:WindDynamicsLookupTable: The current control limitation model with which this wind dynamics lookup table is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'imax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'imaxdip': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mdfslim': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mqpri': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tufilt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindDynamicsLookupTable': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, imax = , imaxdip = , mdfslim = , mqpri = , tufilt = , WindTurbineType3or4IEC = , WindDynamicsLookupTable = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.imax = imax
		self.imaxdip = imaxdip
		self.mdfslim = mdfslim
		self.mqpri = mqpri
		self.tufilt = tufilt
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		
	def __str__(self):
		str = 'class=WindContCurrLimIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
