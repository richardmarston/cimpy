from cimpy.output.DynamicsFunctionBlock import DynamicsFunctionBlock


class UnderexcitationLimiterDynamics(DynamicsFunctionBlock):
	'''
	Underexcitation limiter function block whose behaviour is described by reference to a standard model

	:RemoteInputSignal: Remote input signal used by this underexcitation limiter model. Default: 
	:ExcitationSystemDynamics: Excitation system model with which this underexcitation limiter model is associated. Default: 
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'RemoteInputSignal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = , ExcitationSystemDynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		
	def __str__(self):
		str = 'class=UnderexcitationLimiterDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
