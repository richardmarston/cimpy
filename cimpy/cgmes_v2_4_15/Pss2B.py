from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss2B(PowerSystemStabilizerDynamics):
	'''
	Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).

	:inputSignal1Type: Type of input signal #1.  Typical Value = rotorSpeed. Default: 
	:inputSignal2Type: Type of input signal #2.  Typical Value = generatorElectricalPower. Default: 
	:vsi1max: Input signal #1 max limit (Vsi1max).  Typical Value = 2. Default: 
	:vsi1min: Input signal #1 min limit (Vsi1min).  Typical Value = -2. Default: 
	:tw1: First washout on signal #1 (Tw1).  Typical Value = 2. Default: 
	:tw2: Second washout on signal #1 (Tw2).  Typical Value = 2. Default: 
	:vsi2max: Input signal #2 max limit (Vsi2max).  Typical Value = 2. Default: 
	:vsi2min: Input signal #2 min limit (Vsi2min).  Typical Value = -2. Default: 
	:tw3: First washout on signal #2 (Tw3).  Typical Value = 2. Default: 
	:tw4: Second washout on signal #2 (Tw4).  Typical Value = 0. Default: 
	:t1: Lead/lag time constant (T1).  Typical Value = 0.12. Default: 
	:t2: Lead/lag time constant (T2).  Typical Value = 0.02. Default: 
	:t3: Lead/lag time constant (T3).  Typical Value = 0.3. Default: 
	:t4: Lead/lag time constant (T4).  Typical Value = 0.02. Default: 
	:t6: Time constant on signal #1 (T6).  Typical Value = 0. Default: 
	:t7: Time constant on signal #2 (T7).  Typical Value = 2. Default: 
	:t8: Lead of ramp tracking filter (T8).  Typical Value = 0.2. Default: 
	:t9: Lag of ramp tracking filter (T9).  Typical Value = 0.1. Default: 
	:t10: Lead/lag time constant (T10).  Typical Value = 0. Default: 
	:t11: Lead/lag time constant (T11).  Typical Value = 0. Default: 
	:ks1: Stabilizer gain (Ks1).  Typical Value = 12. Default: 
	:ks2: Gain on signal #2 (Ks2).  Typical Value = 0.2. Default: 
	:ks3: Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1. Default: 
	:ks4: Gain on signal #2 input after ramp-tracking filter (Ks4).  Typical Value = 1. Default: 
	:n: Order of ramp tracking filter (N).  Typical Value = 1. Default: 
	:m: Denominator order of ramp tracking filter (M).  Typical Value = 5. Default: 
	:vstmax: Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 
	:vstmin: Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 
	:a: Numerator constant (a).  Typical Value = 1. Default: 
	:ta: Lead constant (Ta).  Typical Value = 0. Default: 
	:tb: Lag time constant (Tb).  Typical Value = 0. Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignal1Type': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignal2Type': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsi1max': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsi1min': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tw1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tw2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsi2max': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsi2min': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tw3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tw4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't7': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't8': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't9': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't10': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't11': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ks1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ks2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ks3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ks4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'n': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vstmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vstmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignal1Type = , inputSignal2Type = , vsi1max = , vsi1min = , tw1 = , tw2 = , vsi2max = , vsi2min = , tw3 = , tw4 = , t1 = , t2 = , t3 = , t4 = , t6 = , t7 = , t8 = , t9 = , t10 = , t11 = , ks1 = , ks2 = , ks3 = , ks4 = , n = , m = , vstmax = , vstmin = , a = , ta = , tb = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignal1Type = inputSignal1Type
		self.inputSignal2Type = inputSignal2Type
		self.vsi1max = vsi1max
		self.vsi1min = vsi1min
		self.tw1 = tw1
		self.tw2 = tw2
		self.vsi2max = vsi2max
		self.vsi2min = vsi2min
		self.tw3 = tw3
		self.tw4 = tw4
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.t9 = t9
		self.t10 = t10
		self.t11 = t11
		self.ks1 = ks1
		self.ks2 = ks2
		self.ks3 = ks3
		self.ks4 = ks4
		self.n = n
		self.m = m
		self.vstmax = vstmax
		self.vstmin = vstmin
		self.a = a
		self.ta = ta
		self.tb = tb
		
	def __str__(self):
		str = 'class=Pss2B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
