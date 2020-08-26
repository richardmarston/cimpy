from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC3A1(ExcitationSystemDynamics):
	'''
	This is modified old IEEE type 3 excitation system.

	:ka: Voltage regulator gain (Ka).  Typical Value = 300. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.01. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83. Default: 
	:kf: Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675. Default: 
	:kp: Potential circuit gain coefficient (Kp).  Typical Value = 4.37. Default: 
	:ki: Potential circuit gain coefficient (Ki).  Typical Value = 4.83. Default: 
	:vbmax: Available exciter voltage limiter (Vbmax).  Typical Value = 11.63. Default: 
	:exclim: (exclim). true = lower limit of zero is applied to integrator output false = lower limit of zero not applied to integrator output. Typical Value = true. Default: 
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 
	:vb1max: Available exciter voltage limiter (Vb1max).  Typical Value = 11.63. Default: 
	:vblim: Vb limiter indicator. true = exciter Vbmax limiter is active false = Vb1max is active.  Typical Value = true. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vbmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'exclim': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ke': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vb1max': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vblim': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = , ta = , vrmax = , vrmin = , te = , kf = , tf = , kp = , ki = , vbmax = , exclim = , ke = , vb1max = , vblim = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kp = kp
		self.ki = ki
		self.vbmax = vbmax
		self.exclim = exclim
		self.ke = ke
		self.vb1max = vb1max
		self.vblim = vblim
		
	def __str__(self):
		str = 'class=ExcDC3A1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
