from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss1(PowerSystemStabilizerDynamics):
	'''
	Italian PSS - three input PSS (speed, frequency, power).

	:kw: Shaft speed power input gain (K).  Typical Value = 0. Default: 
	:kf: Frequency power input gain (K).  Typical Value = 5. Default: 
	:kpe: Electric power input gain (K).  Typical Value = 0.3. Default: 
	:pmin: Minimum power PSS enabling (P).  Typical Value = 0.25. Default: 
	:ks: PSS gain (K).  Typical Value = 1. Default: 
	:vsmn: Stabilizer output max limit (V).  Typical Value = -0.06. Default: 
	:vsmx: Stabilizer output min limit (V).  Typical Value = 0.06. Default: 
	:tpe: Electric power filter time constant (T).  Typical Value = 0.05. Default: 
	:t5: Washout (T).  Typical Value = 3.5. Default: 
	:t6: Filter time constant (T).  Typical Value = 0. Default: 
	:t7: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:t8: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:t9: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:t10: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:vadat:  Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kw': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'kpe': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'vsmn': [cgmesProfile.DY.value, ],
						'vsmx': [cgmesProfile.DY.value, ],
						'tpe': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						't7': [cgmesProfile.DY.value, ],
						't8': [cgmesProfile.DY.value, ],
						't9': [cgmesProfile.DY.value, ],
						't10': [cgmesProfile.DY.value, ],
						'vadat': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, kw = , kf = , kpe = , pmin = , ks = , vsmn = , vsmx = , tpe = , t5 = , t6 = , t7 = , t8 = , t9 = , t10 = , vadat = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kw = kw
		self.kf = kf
		self.kpe = kpe
		self.pmin = pmin
		self.ks = ks
		self.vsmn = vsmn
		self.vsmx = vsmx
		self.tpe = tpe
		self.t5 = t5
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.t9 = t9
		self.t10 = t10
		self.vadat = vadat
		
	def __str__(self):
		str = 'class=Pss1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
