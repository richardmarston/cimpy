from  import Base


class SvInjection(Base):
	'''
	The SvInjection is reporting the calculated bus injection minus the sum of the terminal flows. The terminal flow is positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection may have the remainder after state estimation or slack after power flow calculation.

	:pInjection: The active power injected into the bus in addition to injections from equipment terminals.  Positive sign means injection into the TopologicalNode (bus). Default: 
	:qInjection: The reactive power injected into the bus in addition to injections from equipment terminals. Positive sign means injection into the TopologicalNode (bus). Default: 
	:TopologicalNode: The injection flows state variables associated with the topological node. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'pInjection': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'qInjection': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'TopologicalNode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, pInjection = , qInjection = , TopologicalNode = ,  ):
	
		self.pInjection = pInjection
		self.qInjection = qInjection
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=SvInjection\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
