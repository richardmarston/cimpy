from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroWPID(TurbineGovernorDynamics):
	'''
	Woodward PID Hydro Governor.

	:mwbase: Base for power values  (MWbase) (>0).  Unit = MW. Default: 
	:treg: Speed detector time constant (Treg). Default: 
	:reg: Permanent drop (Reg). Default: 
	:kp: Proportional gain (Kp).  Typical Value = 0.1. Default: 
	:ki: Reset gain (Ki).  Typical Value = 0.36. Default: 
	:kd: Derivative gain (Kd).  Typical Value = 1.11. Default: 
	:ta: Controller time constant (Ta) (>0).  Typical Value = 0. Default: 
	:tb: Gate servo time constant (Tb) (>0).  Typical Value = 0. Default: 
	:velmax: Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0. Default: 
	:velmin: Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0. Default: 
	:gatmax: Gate opening Limit Maximum (Gatmax). Default: 
	:gatmin: Gate opening Limit Minimum (Gatmin). Default: 
	:tw: Water inertia time constant (Tw) (>0).  Typical Value = 0. Default: 
	:pmax: Maximum Power Output (Pmax). Default: 
	:pmin: Minimum Power Output (Pmin). Default: 
	:d: Turbine damping factor (D).  Unit = delta P / delta speed. Default: 
	:gv3: Gate position 3 (Gv3). Default: 
	:gv1: Gate position 1 (Gv1). Default: 
	:pgv1: Output at Gv1 PU of MWbase (Pgv1). Default: 
	:gv2: Gate position 2 (Gv2). Default: 
	:pgv2: Output at Gv2 PU of MWbase (Pgv2). Default: 
	:pgv3: Output at Gv3 PU of MWbase (Pgv3). Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'treg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'reg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'velmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'velmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gatmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gatmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tw': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , treg = , reg = , kp = , ki = , kd = , ta = , tb = , velmax = , velmin = , gatmax = , gatmin = , tw = , pmax = , pmin = , d = , gv3 = , gv1 = , pgv1 = , gv2 = , pgv2 = , pgv3 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.treg = treg
		self.reg = reg
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.ta = ta
		self.tb = tb
		self.velmax = velmax
		self.velmin = velmin
		self.gatmax = gatmax
		self.gatmin = gatmin
		self.tw = tw
		self.pmax = pmax
		self.pmin = pmin
		self.d = d
		self.gv3 = gv3
		self.gv1 = gv1
		self.pgv1 = pgv1
		self.gv2 = gv2
		self.pgv2 = pgv2
		self.pgv3 = pgv3
		
	def __str__(self):
		str = 'class=GovHydroWPID\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
