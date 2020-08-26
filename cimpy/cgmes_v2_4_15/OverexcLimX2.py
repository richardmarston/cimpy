from cimpy.output.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLimX2(OverexcitationLimiterDynamics):
	'''
	Field Voltage or Current overexcitation limiter designed to protect the generator field of an AC machine with automatic excitation control from overheating due to prolonged overexcitation.

	:m: (m). true = IFD limiting false = EFD limiting. Default: 
	:efdrated: Rated field voltage if m=F or field current if m=T (EFD).  Typical Value = 1.05. Default: 
	:efd1: Low voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.1. Default: 
	:t1: Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME).  Typical Value = 120. Default: 
	:efd2: Mid voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.2. Default: 
	:t2: Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME).  Typical Value = 40. Default: 
	:efd3: High voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.5. Default: 
	:t3: Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME).  Typical Value = 15. Default: 
	:efddes: Desired field voltage if m=F or field current if m=T (EFD).  Typical Value = 1. Default: 
	:kmx: Gain (K).  Typical Value = 0.002. Default: 
	:vlow: Low voltage limit (V) (>0). Default: 
		'''

	cgmesProfile = OverexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdrated': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efd1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efd2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efd3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efddes': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kmx': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vlow': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class OverexcitationLimiterDynamics: \n' + OverexcitationLimiterDynamics.__doc__ 

	def __init__(self, m = , efdrated = , efd1 = , t1 = , efd2 = , t2 = , efd3 = , t3 = , efddes = , kmx = , vlow = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.m = m
		self.efdrated = efdrated
		self.efd1 = efd1
		self.t1 = t1
		self.efd2 = efd2
		self.t2 = t2
		self.efd3 = efd3
		self.t3 = t3
		self.efddes = efddes
		self.kmx = kmx
		self.vlow = vlow
		
	def __str__(self):
		str = 'class=OverexcLimX2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
