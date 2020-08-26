from cimpy.output.GeneratingUnit import GeneratingUnit


class ThermalGeneratingUnit(GeneratingUnit):
	'''
	A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

	:FossilFuels: A thermal generating unit may have one or more fossil fuels. Default: 
		'''

	cgmesProfile = GeneratingUnit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'FossilFuels': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class GeneratingUnit: \n' + GeneratingUnit.__doc__ 

	def __init__(self, FossilFuels = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.FossilFuels = FossilFuels
		
	def __str__(self):
		str = 'class=ThermalGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
