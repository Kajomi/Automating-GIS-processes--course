# first import Shapely module 
from shapely.geometry import Point, LineString, Polygon
import numpy
import types

#---------- Problem - 1 - Creating basic Geometries --------------------------------------

#---------- Section: 1 -------------------------------------------------------------------
# Create a function called createPointGeom() that has two parameters (x_coord, y_coord). 
# Function should create a shapely Point geometry object and return that.
# Demonstrate the usage of the function by creating Point -objects with the function

# creating a function to make Point -objects: 
def createPointGeom(x_coord, y_coord):
	point = Point(x_coord, y_coord)
	return point 

# setting coordinates to implement the function just created:	
helsinki = createPointGeom(60.1, 24.9)
cape_town = createPointGeom(-33.9, 18.2)
nairobi = createPointGeom(-1.3, 36.8)

# printing out the variables to demostrate the function works and returns Point - objects:
print(helsinki)
print(cape_town)
print(nairobi)

# ----------- Section: 2 ------------------------------------------------------------------
# Create a function called createLineGeom() that takes a list of Shapely Point objects as
# parameter and returns a LineString object of those input points. 
# Function should first check that the input list really contains Shapely Point(s). 
# Demonstrate the usage of the function by creating LineString -objects with the function.

# Creating a function that takes a list of points to make a line polygon:
def createLineGeom(x):
	# check if x - argument contains Shapely Point(s):
	# shows the class is a list, how can I check the inside of a list? 
	check = type(x[0]) 
	line = LineString(x)
	print("The type of input is: ", check)
	return line 

# assigning coordinates to varables that represent points in Mannerheimintie:
point1_mansku = Point(60.1, 24.9)
point2_mansku = Point(60.2, 24.8)
point3_mansku = Point(60.3, 24.7)

# implementing the function by assigning Point objects to the function:	
road_mansku = createLineGeom([point1_mansku, point2_mansku, point3_mansku])

# print out the variable: 
print(road_mansku)

#---------- Section: 3 ----------------------------------------------------------------------

# Create a function called createPolyGeom() that takes a list of coordinate tuples OR a list of Shapely Point objects and 
# creates/returns a Polygon object of the input data. Both ways of passing the data to the function should be working. 
# Demonstrate the usage of the function by passing data first with coordinate-tuples and then with Point -objects. 

# create a function:
"""
def createPolyGeom(input): 
		# poly1 should accept only coordinate-tuples as input.
	if isinstance(input, Point):
		polyPoint = Polygon([[coord.x, coord.y] for coord in [input]])
		return polyPoint 
		
		# poly2, only previously defined shapely point -objects.
	else:
		polyTuple = Polygon(input)
		return polyTuple    
	

# create a list of coordinate-tuples to make a Polygon (at least three needed):
list_coords = ([(60.4, 25.3), (60.3, 25.0), (60.2, 25.5)]) 

# create shapely Point -objects to make a Polygon -object:
point1 = Point(60.4, 25.3)
point2 = Point(60.3, 25.0)
point3 = Point(60.2, 25.5)

# implement the function:
polygon_Sipoo_point = createPolyGeom([point1, point2, point3])
polugon_Sipoo_tuple = createPolyGeom([(60.4, 25.3), (60.3, 25.0), (60.2, 25.5)])

# print out to demostrate the function accepts both types of input and returns a Polygon -object:
print(polygon_Sipoo_point)
print(polygon_Sipoo_tuple)

# Just keeps giving me TypeError: object of type 'Point' has no len() 
"""








































