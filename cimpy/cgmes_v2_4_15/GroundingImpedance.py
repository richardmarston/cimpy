from cimpy.output.EarthFaultCompensator import EarthFaultCompensator


class GroundingImpedance(EarthFaultCompensator):
	'''
	A fixed impedance device used for grounding.

	:x: Reactance of device. Default: 
		'''

	cgmesProfile = EarthFaultCompensator.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'x': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EarthFaultCompensator: \n' + EarthFaultCompensator.__doc__ 

	def __init__(self, x = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.x = x
		
	def __str__(self):
		str = 'class=GroundingImpedance\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
