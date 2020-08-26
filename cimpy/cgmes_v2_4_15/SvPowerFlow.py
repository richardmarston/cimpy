from  import Base


class SvPowerFlow(Base):
	'''
	State variable for power flow. Load convention is used for flow direction. This means flow out from the TopologicalNode into the equipment is positive.

	:Terminal: The terminal associated with the power flow state variable. Default: 
	:p: The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 
	:q: The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'Terminal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'p': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'q': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, Terminal = , p = , q = ,  ):
	
		self.Terminal = Terminal
		self.p = p
		self.q = q
		
	def __str__(self):
		str = 'class=SvPowerFlow\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
