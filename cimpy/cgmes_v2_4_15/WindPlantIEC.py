from cimpy.output.WindPlantDynamics import WindPlantDynamics


class WindPlantIEC(WindPlantDynamics):
	'''
	Simplified IEC type plant level model.   Reference: IEC 61400-27-1, AnnexE.

	:WindPlantFreqPcontrolIEC: Wind plant frequency and active power control model associated with this wind plant. Default: 
	:WindPlantReactiveControlIEC: Wind plant reactive control model associated with this wind plant. Default: 
		'''

	cgmesProfile = WindPlantDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindPlantFreqPcontrolIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindPlantReactiveControlIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindPlantDynamics: \n' + WindPlantDynamics.__doc__ 

	def __init__(self, WindPlantFreqPcontrolIEC = , WindPlantReactiveControlIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindPlantFreqPcontrolIEC = WindPlantFreqPcontrolIEC
		self.WindPlantReactiveControlIEC = WindPlantReactiveControlIEC
		
	def __str__(self):
		str = 'class=WindPlantIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
