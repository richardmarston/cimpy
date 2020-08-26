from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssPTIST1(PowerSystemStabilizerDynamics):
	'''
	PTI Microprocessor-Based Stabilizer type 1.

	:m: (M).  M=2*H.  Typical Value = 5. Default: 
	:tf: Time constant (Tf).  Typical Value = 0.2. Default: 
	:tp: Time constant (Tp).  Typical Value = 0.2. Default: 
	:t1: Time constant (T1).  Typical Value = 0.3. Default: 
	:t2: Time constant (T2).  Typical Value = 1. Default: 
	:t3: Time constant (T3).  Typical Value = 0.2. Default: 
	:t4: Time constant (T4).  Typical Value = 0.05. Default: 
	:k: Gain (K).  Typical Value = 9. Default: 
	:dtf: Time step frequency calculation (Dtf).  Typical Value = 0.025. Default: 
	:dtc: Time step related to activation of controls (Dtc).  Typical Value = 0.025. Default: 
	:dtp: Time step active power calculation (Dtp).  Typical Value = 0.0125. Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dtf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dtc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dtp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, m = , tf = , tp = , t1 = , t2 = , t3 = , t4 = , k = , dtf = , dtc = , dtp = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.m = m
		self.tf = tf
		self.tp = tp
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.k = k
		self.dtf = dtf
		self.dtc = dtc
		self.dtp = dtp
		
	def __str__(self):
		str = 'class=PssPTIST1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
