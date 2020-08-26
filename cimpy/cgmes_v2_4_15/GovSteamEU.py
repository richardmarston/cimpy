from cimpy.cgmes_v2_4_15.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamEU(TurbineGovernorDynamics):
	'''
	Simplified model  of boiler and steam turbine with PID governor.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:tp: Power transducer time constant (Tp).  Typical Value = 0.07. Default: 
	:ke: Gain of the power controller (Ke).  Typical Value = 0.65. Default: 
	:tip: Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 
	:tdp: Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 
	:tfp: Time constant of the power controller (Tfp).  Typical Value = 0. Default: 
	:tf: Frequency transducer time constant (Tf).  Typical Value = 0. Default: 
	:kfcor: Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 
	:db1: Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 
	:wfmax: Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 
	:wfmin: Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 
	:pmax: Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 
	:ten: Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 
	:tw: Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 
	:kwcor: Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 
	:db2: Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 
	:wwmax: Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 
	:wwmin: Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 
	:wmax1: Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 
	:wmax2: Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 
	:tvhp: Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 
	:cho: Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 
	:chc: Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 
	:hhpmax: Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 
	:tvip: Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 
	:cio: Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 
	:cic: Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 
	:simx: Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 
	:thp: High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 
	:trh: Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 
	:tlp: Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 
	:prhmax: Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 
	:khp: Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 
	:klp: Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 
	:tb: Boiler time constant (Tb).  Typical Value = 100. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'tip': [cgmesProfile.DY.value, ],
						'tdp': [cgmesProfile.DY.value, ],
						'tfp': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kfcor': [cgmesProfile.DY.value, ],
						'db1': [cgmesProfile.DY.value, ],
						'wfmax': [cgmesProfile.DY.value, ],
						'wfmin': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'ten': [cgmesProfile.DY.value, ],
						'tw': [cgmesProfile.DY.value, ],
						'kwcor': [cgmesProfile.DY.value, ],
						'db2': [cgmesProfile.DY.value, ],
						'wwmax': [cgmesProfile.DY.value, ],
						'wwmin': [cgmesProfile.DY.value, ],
						'wmax1': [cgmesProfile.DY.value, ],
						'wmax2': [cgmesProfile.DY.value, ],
						'tvhp': [cgmesProfile.DY.value, ],
						'cho': [cgmesProfile.DY.value, ],
						'chc': [cgmesProfile.DY.value, ],
						'hhpmax': [cgmesProfile.DY.value, ],
						'tvip': [cgmesProfile.DY.value, ],
						'cio': [cgmesProfile.DY.value, ],
						'cic': [cgmesProfile.DY.value, ],
						'simx': [cgmesProfile.DY.value, ],
						'thp': [cgmesProfile.DY.value, ],
						'trh': [cgmesProfile.DY.value, ],
						'tlp': [cgmesProfile.DY.value, ],
						'prhmax': [cgmesProfile.DY.value, ],
						'khp': [cgmesProfile.DY.value, ],
						'klp': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , tp = , ke = , tip = , tdp = , tfp = , tf = , kfcor = , db1 = , wfmax = , wfmin = , pmax = , ten = , tw = , kwcor = , db2 = , wwmax = , wwmin = , wmax1 = , wmax2 = , tvhp = , cho = , chc = , hhpmax = , tvip = , cio = , cic = , simx = , thp = , trh = , tlp = , prhmax = , khp = , klp = , tb = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.tp = tp
		self.ke = ke
		self.tip = tip
		self.tdp = tdp
		self.tfp = tfp
		self.tf = tf
		self.kfcor = kfcor
		self.db1 = db1
		self.wfmax = wfmax
		self.wfmin = wfmin
		self.pmax = pmax
		self.ten = ten
		self.tw = tw
		self.kwcor = kwcor
		self.db2 = db2
		self.wwmax = wwmax
		self.wwmin = wwmin
		self.wmax1 = wmax1
		self.wmax2 = wmax2
		self.tvhp = tvhp
		self.cho = cho
		self.chc = chc
		self.hhpmax = hhpmax
		self.tvip = tvip
		self.cio = cio
		self.cic = cic
		self.simx = simx
		self.thp = thp
		self.trh = trh
		self.tlp = tlp
		self.prhmax = prhmax
		self.khp = khp
		self.klp = klp
		self.tb = tb
		
	def __str__(self):
		str = 'class=GovSteamEU\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
