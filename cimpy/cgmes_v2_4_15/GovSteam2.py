from cimpy.cgmes_v2_4_15.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam2(TurbineGovernorDynamics):
	'''
	Simplified governor model.

	:k: Governor gain (reciprocal of droop) (K).  Typical Value = 20. Default: 
	:dbf: Frequency dead band (DBF).  Typical Value = 0. Default: 
	:t1: Governor lag time constant (T) (>0).  Typical Value = 0.45. Default: 
	:t2: Governor lead time constant (T) (may be 0).  Typical Value = 0. Default: 
	:pmax: Maximum fuel flow (P).  Typical Value = 1. Default: 
	:pmin: Minimum fuel flow (P).  Typical Value = 0. Default: 
	:mxef: Fuel flow maximum positive error value (MX).  Typical Value = 1. Default: 
	:mnef: Fuel flow maximum negative error value (MN).  Typical Value = -1. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						'dbf': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'mxef': [cgmesProfile.DY.value, ],
						'mnef': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, k = , dbf = , t1 = , t2 = , pmax = , pmin = , mxef = , mnef = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k = k
		self.dbf = dbf
		self.t1 = t1
		self.t2 = t2
		self.pmax = pmax
		self.pmin = pmin
		self.mxef = mxef
		self.mnef = mnef
		
	def __str__(self):
		str = 'class=GovSteam2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
