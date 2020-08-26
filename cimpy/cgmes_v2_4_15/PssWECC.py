from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssWECC(PowerSystemStabilizerDynamics):
	'''
	Dual input Power System Stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western Electricity Coordinating Council, USA).

	:inputSignal1Type: Type of input signal #1. Default: 
	:inputSignal2Type: Type of input signal #2. Default: 
	:k1: Input signal 1 gain  (K). Default: 
	:t1: Input signal 1 transducer time constant (T). Default: 
	:k2: Input signal 2 gain (K). Default: 
	:t2: Input signal 2 transducer time constant (T). Default: 
	:t3: Stabilizer washout time constant (T). Default: 
	:t4: Stabilizer washout time lag constant (T) (>0). Default: 
	:t5: Lead time constant (T). Default: 
	:t6: Lag time constant (T). Default: 
	:t7: Lead time constant (T). Default: 
	:t8: Lag time constant (T). Default: 
	:t10: Lag time constant (T). Default: 
	:t9: Lead time constant (T). Default: 
	:vsmax: Maximum output signal (Vsmax). Default: 
	:vsmin: Minimum output signal (Vsmin). Default: 
	:vcu: Maximum value for voltage compensator output (V). Default: 
	:vcl: Minimum value for voltage compensator output (V). Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignal1Type': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignal2Type': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't7': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't8': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't10': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't9': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vcu': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vcl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignal1Type = , inputSignal2Type = , k1 = , t1 = , k2 = , t2 = , t3 = , t4 = , t5 = , t6 = , t7 = , t8 = , t10 = , t9 = , vsmax = , vsmin = , vcu = , vcl = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignal1Type = inputSignal1Type
		self.inputSignal2Type = inputSignal2Type
		self.k1 = k1
		self.t1 = t1
		self.k2 = k2
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.t10 = t10
		self.t9 = t9
		self.vsmax = vsmax
		self.vsmin = vsmin
		self.vcu = vcu
		self.vcl = vcl
		
	def __str__(self):
		str = 'class=PssWECC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
