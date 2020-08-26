from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroR(TurbineGovernorDynamics):
	'''
	Fourth order lead-lag governor and hydro turbine.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:pmax: Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 
	:pmin: Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 
	:r: Steady-state droop (R).  Typical Value = 0.05. Default: 
	:td: Input filter time constant (Td).  Typical Value = 0.05. Default: 
	:t1: Lead time constant 1 (T1).  Typical Value = 1.5. Default: 
	:t2: Lag time constant 1 (T2).  Typical Value = 0.1. Default: 
	:t3: Lead time constant 2 (T3).  Typical Value = 1.5. Default: 
	:t4: Lag time constant 2 (T4).  Typical Value = 0.1. Default: 
	:t5: Lead time constant 3 (T5).  Typical Value = 0. Default: 
	:t6: Lag time constant 3 (T6).  Typical Value = 0.05. Default: 
	:t7: Lead time constant 4 (T7).  Typical Value = 0. Default: 
	:t8: Lag time constant 4 (T8).  Typical Value = 0.05. Default: 
	:tp: Gate servo time constant (Tp).  Typical Value = 0.05. Default: 
	:velop: Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.2. Default: 
	:velcl: Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2. Default: 
	:ki: Integral gain (Ki).  Typical Value = 0.5. Default: 
	:kg: Gate servo gain (Kg).  Typical Value = 2. Default: 
	:gmax: Maximum governor output (Gmax).  Typical Value = 1.05. Default: 
	:gmin: Minimum governor output (Gmin).  Typical Value = -0.05. Default: 
	:tt: Power feedback time constant (Tt).  Typical Value = 0. Default: 
	:inputSignal: Input signal switch (Flag). true = Pe input is used false = feedback is received from CV. Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to true.  Typical Value = true. Default: 
	:db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 
	:eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 
	:db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 
	:tw: Water inertia time constant (Tw).  Typical Value = 1. Default: 
	:at: Turbine gain (At).  Typical Value = 1.2. Default: 
	:dturb: Turbine damping factor (Dturb).  Typical Value = 0.2. Default: 
	:qnl: No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08. Default: 
	:h0: Turbine nominal head (H0).  Typical Value = 1. Default: 
	:gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 
	:pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 
	:gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 
	:pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 
	:gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 
	:pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 
	:gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 
	:pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 
	:gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 
	:pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 
	:gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 
	:pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'r': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'td': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't7': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't8': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'velop': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'velcl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'db1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eps': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'db2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tw': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'at': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dturb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qnl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'h0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'gv6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pgv6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , pmax = , pmin = , r = , td = , t1 = , t2 = , t3 = , t4 = , t5 = , t6 = , t7 = , t8 = , tp = , velop = , velcl = , ki = , kg = , gmax = , gmin = , tt = , inputSignal = , db1 = , eps = , db2 = , tw = , at = , dturb = , qnl = , h0 = , gv1 = , pgv1 = , gv2 = , pgv2 = , gv3 = , pgv3 = , gv4 = , pgv4 = , gv5 = , pgv5 = , gv6 = , pgv6 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.pmax = pmax
		self.pmin = pmin
		self.r = r
		self.td = td
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.tp = tp
		self.velop = velop
		self.velcl = velcl
		self.ki = ki
		self.kg = kg
		self.gmax = gmax
		self.gmin = gmin
		self.tt = tt
		self.inputSignal = inputSignal
		self.db1 = db1
		self.eps = eps
		self.db2 = db2
		self.tw = tw
		self.at = at
		self.dturb = dturb
		self.qnl = qnl
		self.h0 = h0
		self.gv1 = gv1
		self.pgv1 = pgv1
		self.gv2 = gv2
		self.pgv2 = pgv2
		self.gv3 = gv3
		self.pgv3 = pgv3
		self.gv4 = gv4
		self.pgv4 = pgv4
		self.gv5 = gv5
		self.pgv5 = pgv5
		self.gv6 = gv6
		self.pgv6 = pgv6
		
	def __str__(self):
		str = 'class=GovHydroR\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
