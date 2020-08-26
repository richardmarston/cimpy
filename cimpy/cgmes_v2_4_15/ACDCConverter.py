from cimpy.output.ConductingEquipment import ConductingEquipment


class ACDCConverter(ConductingEquipment):
	'''
	A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

	:baseS: Base apparent power of the converter pole. Default: 
	:idleLoss: Active power loss in pole at no power transfer. Converter configuration data used in power flow. Default: 
	:maxUdc: The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow. Default: 
	:minUdc: Min allowed converter DC voltage. Converter configuration data used in power flow. Default: 
	:numberOfValves: Number of valves in the converter. Used in loss calculations. Default: 
	:ratedUdc: Rated converter DC voltage, also called UdN. Converter configuration data used in power flow. Default: 
	:resistiveLoss: Converter configuration data used in power flow. Refer to poleLossP. Default: 
	:switchingLoss: Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. Default: 
	:valveU0: Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 
	:DCTerminals:  Default: 
	:PccTerminal: All converters` DC sides linked to this point of common coupling terminal. Default: 
	:p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 
	:q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 
	:targetPpcc: Real power injection target in AC grid, at point of common coupling. Default: 
	:targetUdc: Target value for DC voltage magnitude. Default: 
	:idc: Converter DC current, also called Id. Converter state variable, result from power flow. Default: 
	:poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with losses Pdc=Pac+lossP Converter state variable used in power flow. Default: 
	:uc: Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow. Default: 
	:udc: Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow. Default: 
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'baseS': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'idleLoss': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'maxUdc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'minUdc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'numberOfValves': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ratedUdc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'resistiveLoss': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'switchingLoss': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'valveU0': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'DCTerminals': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'PccTerminal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'p': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'q': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'targetPpcc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'targetUdc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'idc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'poleLossP': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'uc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'udc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, baseS = , idleLoss = , maxUdc = , minUdc = , numberOfValves = , ratedUdc = , resistiveLoss = , switchingLoss = , valveU0 = , DCTerminals = , PccTerminal = , p = , q = , targetPpcc = , targetUdc = , idc = , poleLossP = , uc = , udc = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.baseS = baseS
		self.idleLoss = idleLoss
		self.maxUdc = maxUdc
		self.minUdc = minUdc
		self.numberOfValves = numberOfValves
		self.ratedUdc = ratedUdc
		self.resistiveLoss = resistiveLoss
		self.switchingLoss = switchingLoss
		self.valveU0 = valveU0
		self.DCTerminals = DCTerminals
		self.PccTerminal = PccTerminal
		self.p = p
		self.q = q
		self.targetPpcc = targetPpcc
		self.targetUdc = targetUdc
		self.idc = idc
		self.poleLossP = poleLossP
		self.uc = uc
		self.udc = udc
		
	def __str__(self):
		str = 'class=ACDCConverter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
