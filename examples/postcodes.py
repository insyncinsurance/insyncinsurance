from src.insync.insync import *


PolicyPostcode = Postcodes('BH17 7BX') # Create a new Postcodes object. String can be replaced with the Workbench 'Postcode' field.

PolicyPostcode.area() # Returns the area of the Postcode.
PolicyPostcode.district() # Returns the district of the Postcode.
PolicyPostcode.sector() # Returns the sector of the Postcode.
PolicyPostcode.unit() # Returns the unit of the Postcode.

PolicyPostcode.contains('BH17') # Returns True if the Postcode contains the string 'BH17'.
PolicyPostcode.contains(['BH17', 'BH17A']) # Returns True if the Postcode contains either 'BH17' or 'BH17A'.