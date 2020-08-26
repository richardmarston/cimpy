from cimpy.output.IdentifiedObject import IdentifiedObject


class WindContQIEC(IdentifiedObject):
	'''
	Q control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.6.

	:iqh1: Maximum reactive current injection during dip (i). It is type dependent parameter. Default: 
	:iqmax: Maximum reactive current injection (i). It is type dependent parameter. Default: 
	:iqmin: Minimum reactive current injection (i). It is type dependent parameter. Default: 
	:iqpost: Post fault reactive current injection (). It is project dependent parameter. Default: 
	:kiq: Reactive power PI controller integration gain (). It is type dependent parameter. Default: 
	:kiu: Voltage PI controller integration gain (). It is type dependent parameter. Default: 
	:kpq: Reactive power PI controller proportional gain (). It is type dependent parameter. Default: 
	:kpu: Voltage PI controller proportional gain (). It is type dependent parameter. Default: 
	:kqv: Voltage scaling factor for LVRT current (). It is project dependent parameter. Default: 
	:qmax: Maximum reactive power (q). It is type dependent parameter. Default: 
	:qmin: Minimum reactive power (q). It is type dependent parameter. Default: 
	:rdroop: Resistive component of voltage drop impedance (). It is project dependent parameter. Default: 
	:tiq: Time constant in reactive current lag (T). It is type dependent parameter. Default: 
	:tpfilt: Power measurement filter time constant (). It is type dependent parameter. Default: 
	:tpost: Length of time period where post fault reactive power is injected (). It is project dependent parameter. Default: 
	:tqord: Time constant in reactive power order lag (). It is type dependent parameter. Default: 
	:tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 
	:udb1: Voltage dead band lower limit (). It is type dependent parameter. Default: 
	:udb2: Voltage dead band upper limit (). It is type dependent parameter. Default: 
	:umax: Maximum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 
	:umin: Minimum voltage in voltage PI controller integral term (u). It is type dependent parameter. Default: 
	:uqdip: Voltage threshold for LVRT detection in q control (). It is type dependent parameter. Default: 
	:uref0: User defined bias in voltage reference (), used when  =. It is case dependent parameter. Default: 
	:windLVRTQcontrolModesType: Types of LVRT Q control modes (). It is project dependent parameter. Default: 
	:windQcontrolModesType: Types of general wind turbine Q control modes ().  It is project dependent parameter. Default: 
	:xdroop: Inductive component of voltage drop impedance (). It is project dependent parameter. Default: 
	:WindTurbineType3or4IEC: Wind turbine type 3 or 4 model with which this reactive control mode is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'iqh1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'iqmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'iqmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'iqpost': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kiq': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kiu': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpq': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpu': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kqv': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'rdroop': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tiq': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpfilt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpost': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tqord': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tufilt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'udb1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'udb2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'umax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'umin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uqdip': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uref0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'windLVRTQcontrolModesType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'windQcontrolModesType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xdroop': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, iqh1 = , iqmax = , iqmin = , iqpost = , kiq = , kiu = , kpq = , kpu = , kqv = , qmax = , qmin = , rdroop = , tiq = , tpfilt = , tpost = , tqord = , tufilt = , udb1 = , udb2 = , umax = , umin = , uqdip = , uref0 = , windLVRTQcontrolModesType = , windQcontrolModesType = , xdroop = , WindTurbineType3or4IEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.iqh1 = iqh1
		self.iqmax = iqmax
		self.iqmin = iqmin
		self.iqpost = iqpost
		self.kiq = kiq
		self.kiu = kiu
		self.kpq = kpq
		self.kpu = kpu
		self.kqv = kqv
		self.qmax = qmax
		self.qmin = qmin
		self.rdroop = rdroop
		self.tiq = tiq
		self.tpfilt = tpfilt
		self.tpost = tpost
		self.tqord = tqord
		self.tufilt = tufilt
		self.udb1 = udb1
		self.udb2 = udb2
		self.umax = umax
		self.umin = umin
		self.uqdip = uqdip
		self.uref0 = uref0
		self.windLVRTQcontrolModesType = windLVRTQcontrolModesType
		self.windQcontrolModesType = windQcontrolModesType
		self.xdroop = xdroop
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		
	def __str__(self):
		str = 'class=WindContQIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
