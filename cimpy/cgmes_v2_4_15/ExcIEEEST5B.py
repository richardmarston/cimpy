from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST5B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits.  Reference: IEEE Standard 421.5-2005 Section 7.5.   Note: the block diagram in the IEEE 421.5 standard has input signal Vc and does not indicate the summation point with Vref. The implementation of the ExcIEEEST5B shall consider summation point with Vref.

	:kr: Regulator gain (K).  Typical Value = 200. Default: 
	:t1: Firing circuit time constant (T1).  Typical Value = 0.004. Default: 
	:kc: Rectifier regulation factor (K).  Typical Value = 0.004. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 5. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -4. Default: 
	:tc1: Regulator lead time constant (T).  Typical Value = 0.8. Default: 
	:tb1: Regulator lag time constant (T).  Typical Value = 6. Default: 
	:tc2: Regulator lead time constant (T).  Typical Value = 0.08. Default: 
	:tb2: Regulator lag time constant (T).  Typical Value = 0.01. Default: 
	:toc1: OEL lead time constant (T).  Typical Value = 0.1. Default: 
	:tob1: OEL lag time constant (T).  Typical Value = 2. Default: 
	:toc2: OEL lead time constant (T).  Typical Value = 0.08. Default: 
	:tob2: OEL lag time constant (T).  Typical Value = 0.08. Default: 
	:tuc1: UEL lead time constant (T).  Typical Value = 2. Default: 
	:tub1: UEL lag time constant (T).  Typical Value = 10. Default: 
	:tuc2: UEL lead time constant (T).  Typical Value = 0.1. Default: 
	:tub2: UEL lag time constant (T).  Typical Value = 0.05. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'toc1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tob1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'toc2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tob2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tuc1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tub1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tuc2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tub2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kr = , t1 = , kc = , vrmax = , vrmin = , tc1 = , tb1 = , tc2 = , tb2 = , toc1 = , tob1 = , toc2 = , tob2 = , tuc1 = , tub1 = , tuc2 = , tub2 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kr = kr
		self.t1 = t1
		self.kc = kc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.tc1 = tc1
		self.tb1 = tb1
		self.tc2 = tc2
		self.tb2 = tb2
		self.toc1 = toc1
		self.tob1 = tob1
		self.toc2 = toc2
		self.tob2 = tob2
		self.tuc1 = tuc1
		self.tub1 = tub1
		self.tuc2 = tuc2
		self.tub2 = tub2
		
	def __str__(self):
		str = 'class=ExcIEEEST5B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
