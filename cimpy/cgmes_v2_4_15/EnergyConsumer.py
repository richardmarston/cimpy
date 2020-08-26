from cimpy.output.ConductingEquipment import ConductingEquipment


class EnergyConsumer(ConductingEquipment):
	'''
	Generic user of energy - a  point of consumption on the power system model.

	:LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power. Default: 
	:pfixed: Active power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 
	:pfixedPct: Fixed active power as per cent of load group fixed active power. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 
	:qfixed: Reactive power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 
	:qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 
	:p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 
	:q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 
	:LoadDynamics: Load dynamics model used to describe dynamic behavior of this energy consumer. Default: 
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'LoadResponse': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'pfixed': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'pfixedPct': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'qfixed': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'qfixedPct': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'p': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'q': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'LoadDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, LoadResponse = , pfixed = , pfixedPct = , qfixed = , qfixedPct = , p = , q = , LoadDynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadResponse = LoadResponse
		self.pfixed = pfixed
		self.pfixedPct = pfixedPct
		self.qfixed = qfixed
		self.qfixedPct = qfixedPct
		self.p = p
		self.q = q
		self.LoadDynamics = LoadDynamics
		
	def __str__(self):
		str = 'class=EnergyConsumer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
