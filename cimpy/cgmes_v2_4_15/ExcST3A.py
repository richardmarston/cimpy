from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST3A(ExcitationSystemDynamics):
	'''
	Modified IEEE ST3A static excitation system with added speed multiplier.

	:vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 0.2. Default: 
	:vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -0.2. Default: 
	:kj: AVR gain (Kj).  Typical Value = 200. Default: 
	:tb: Voltage regulator time constant (Tb).  Typical Value = 6.67. Default: 
	:tc: Voltage regulator time constant (Tc).  Typical Value = 1. Default: 
	:efdmax: Maximum AVR output (Efdmax).  Typical Value = 6.9. Default: 
	:km: Forward gain constant of the inner loop field regulator (Km).  Typical Value = 7.04. Default: 
	:tm: Forward time constant of inner loop field regulator (Tm).  Typical Value = 1. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 
	:kg: Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1. Default: 
	:kp: Potential source gain (Kp) (>0).  Typical Value = 4.37. Default: 
	:thetap: Potential circuit phase angle (thetap).  Typical Value = 20. Default: 
	:ki: Potential circuit gain coefficient (Ki).  Typical Value = 4.83. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 1.1. Default: 
	:xl: Reactance associated with potential source (Xl).  Typical Value = 0.09. Default: 
	:vbmax: Maximum excitation voltage (Vbmax).  Typical Value = 8.63. Default: 
	:vgmax: Maximum inner loop feedback voltage (Vgmax).  Typical Value = 6.53. Default: 
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 
	:ks1: Coefficient to allow different usage of the model-speed coefficient (Ks1).  Typical Value = 0. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'kj': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						'km': [cgmesProfile.DY.value, ],
						'tm': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'thetap': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'xl': [cgmesProfile.DY.value, ],
						'vbmax': [cgmesProfile.DY.value, ],
						'vgmax': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'ks1': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, vimax = , vimin = , kj = , tb = , tc = , efdmax = , km = , tm = , vrmax = , vrmin = , kg = , kp = , thetap = , ki = , kc = , xl = , vbmax = , vgmax = , ks = , ks1 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vimax = vimax
		self.vimin = vimin
		self.kj = kj
		self.tb = tb
		self.tc = tc
		self.efdmax = efdmax
		self.km = km
		self.tm = tm
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kg = kg
		self.kp = kp
		self.thetap = thetap
		self.ki = ki
		self.kc = kc
		self.xl = xl
		self.vbmax = vbmax
		self.vgmax = vgmax
		self.ks = ks
		self.ks1 = ks1
		
	def __str__(self):
		str = 'class=ExcST3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
