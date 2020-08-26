from cimpy.output.RegularIntervalSchedule import RegularIntervalSchedule


class SeasonDayTypeSchedule(RegularIntervalSchedule):
	'''
	A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

	:DayType: Schedules that use this DayType. Default: 
	:Season: Schedules that use this Season. Default: 
		'''

	cgmesProfile = RegularIntervalSchedule.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'DayType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Season': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RegularIntervalSchedule: \n' + RegularIntervalSchedule.__doc__ 

	def __init__(self, DayType = , Season = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DayType = DayType
		self.Season = Season
		
	def __str__(self):
		str = 'class=SeasonDayTypeSchedule\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
