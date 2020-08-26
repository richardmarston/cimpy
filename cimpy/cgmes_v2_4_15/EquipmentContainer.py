from cimpy.output.ConnectivityNodeContainer import ConnectivityNodeContainer


class EquipmentContainer(ConnectivityNodeContainer):
	'''
	A modeling construct to provide a root class for containing equipment.

	:Equipments: Contained equipment. Default: 
		'''

	cgmesProfile = ConnectivityNodeContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'Equipments': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConnectivityNodeContainer: \n' + ConnectivityNodeContainer.__doc__ 

	def __init__(self, Equipments = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Equipments = Equipments
		
	def __str__(self):
		str = 'class=EquipmentContainer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
