from cimpy.output.GeneratingUnit import GeneratingUnit


class HydroGeneratingUnit(GeneratingUnit):
	'''
	A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

	:energyConversionCapability: Energy conversion capability for generating. Default: 
	:HydroPowerPlant: The hydro generating unit belongs to a hydro power plant. Default: 
		'''

	cgmesProfile = GeneratingUnit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'energyConversionCapability': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'HydroPowerPlant': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class GeneratingUnit: \n' + GeneratingUnit.__doc__ 

	def __init__(self, energyConversionCapability = , HydroPowerPlant = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.energyConversionCapability = energyConversionCapability
		self.HydroPowerPlant = HydroPowerPlant
		
	def __str__(self):
		str = 'class=HydroGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
