from cimpy.output.DynamicsFunctionBlock import DynamicsFunctionBlock


class RotatingMachineDynamics(DynamicsFunctionBlock):
	'''
	Abstract parent class for all synchronous and asynchronous machine standard models.

	:damping: Damping torque coefficient (D).  A proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.  This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modelled in detail.  Typical Value = 0. Default: 
	:inertia: Inertia constant of generator or motor and mechanical load (H) (>0).  This is the specification for the stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the generator plus all other elements (turbine, exciter) on the same shaft and has units of MW*sec.  For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW*second/MVA or just second.   This value is used in the accelerating power reference frame for operator training simulator solutions.  Typical Value = 3. Default: 
	:saturationFactor: Saturation factor at rated terminal voltage (S1) (> or =0).  Not used by simplified model.  Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical Value = 0.02. Default: 
	:saturationFactor120: Saturation factor at 120% of rated terminal voltage (S12) (> or =S1). Not used by the simplified model, defined by S(E2) in the SynchronousMachineSaturationParameters diagram.  Typical Value = 0.12. Default: 
	:statorLeakageReactance: Stator leakage reactance (Xl) (> or =0). Typical Value = 0.15. Default: 
	:statorResistance: Stator (armature) resistance (Rs) (> or =0). Typical Value = 0.005. Default: 
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'damping': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inertia': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'saturationFactor': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'saturationFactor120': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'statorLeakageReactance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'statorResistance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, damping = , inertia = , saturationFactor = , saturationFactor120 = , statorLeakageReactance = , statorResistance = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.damping = damping
		self.inertia = inertia
		self.saturationFactor = saturationFactor
		self.saturationFactor120 = saturationFactor120
		self.statorLeakageReactance = statorLeakageReactance
		self.statorResistance = statorResistance
		
	def __str__(self):
		str = 'class=RotatingMachineDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
