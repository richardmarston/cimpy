from cimpy.output.TurbineLoadControllerDynamics import TurbineLoadControllerDynamics


class TurbineLoadControllerUserDefined(TurbineLoadControllerDynamics):
	'''
	Turbine load controller function block whose dynamic behaviour is described by

	:proprietary: Behaviour is based on proprietary model as opposed to detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. Default: 
	:ProprietaryParameterDynamics: Parameter of this proprietary user-defined model. Default: 
		'''

	cgmesProfile = TurbineLoadControllerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'proprietary': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ProprietaryParameterDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineLoadControllerDynamics: \n' + TurbineLoadControllerDynamics.__doc__ 

	def __init__(self, proprietary = , ProprietaryParameterDynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.proprietary = proprietary
		self.ProprietaryParameterDynamics = ProprietaryParameterDynamics
		
	def __str__(self):
		str = 'class=TurbineLoadControllerUserDefined\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
