from  import Base


class DiagramObjectPoint(Base):
	'''
	A point in a given space defined by 3 coordinates and associated to a diagram object.  The coordinates may be positive or negative as the origin does not have to be in the corner of a diagram.

	:DiagramObject: The diagram object with which the points are associated. Default: 
	:DiagramObjectGluePoint: A diagram object glue point is associated with 2 or more object points that are considered to be `glued` together. Default: 
	:sequenceNumber: The sequence position of the point, used for defining the order of points for diagram objects acting as a polyline or polygon with more than one point. Default: 
	:xPosition: The X coordinate of this point. Default: 
	:yPosition: The Y coordinate of this point. Default: 
	:zPosition: The Z coordinate of this point. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'DiagramObject': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'DiagramObjectGluePoint': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'sequenceNumber': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'xPosition': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'yPosition': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						'zPosition': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DL'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, DiagramObject = , DiagramObjectGluePoint = , sequenceNumber = , xPosition = , yPosition = , zPosition = ,  ):
	
		self.DiagramObject = DiagramObject
		self.DiagramObjectGluePoint = DiagramObjectGluePoint
		self.sequenceNumber = sequenceNumber
		self.xPosition = xPosition
		self.yPosition = yPosition
		self.zPosition = zPosition
		
	def __str__(self):
		str = 'class=DiagramObjectPoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
