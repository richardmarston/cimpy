from cimpy.output.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
	'''
	The class represents IEEE PF Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.2.

	:ovex: Overexcitation Flag () true = overexcited false = underexcited. Default: 
	:tpfc: PF controller time delay ().  Typical Value = 5. Default: 
	:vitmin: Minimum machine terminal current needed to enable pf/var controller (). Default: 
	:vpf: Synchronous machine power factor (). Default: 
	:vpfcbw: PF controller dead band ().  Typical Value = 0.05. Default: 
	:vpfref: PF controller reference (). Default: 
	:vvtmax: Maximum machine terminal voltage needed for pf/var controller to be enabled (). Default: 
	:vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (). Default: 
		'''

	cgmesProfile = PFVArControllerType1Dynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ovex': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpfc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vitmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vpf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vpfcbw': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vpfref': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vvtmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vvtmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PFVArControllerType1Dynamics: \n' + PFVArControllerType1Dynamics.__doc__ 

	def __init__(self, ovex = , tpfc = , vitmin = , vpf = , vpfcbw = , vpfref = , vvtmax = , vvtmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ovex = ovex
		self.tpfc = tpfc
		self.vitmin = vitmin
		self.vpf = vpf
		self.vpfcbw = vpfcbw
		self.vpfref = vpfref
		self.vvtmax = vvtmax
		self.vvtmin = vvtmin
		
	def __str__(self):
		str = 'class=PFVArType1IEEEPFController\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
