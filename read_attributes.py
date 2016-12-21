#-------------- Problem - 2 - Attributes of Geometries -------------------------------------------------------------------

#------- Section: 1 ---------------------------------------------------------------------------

# Create a function called getCentroid() that takes any kind of Shapely's geometric -object as input and returns a 
# centroid of that geometry. Demonstrate the usage of the function.

from shapely.geometry import Point, LineString, Polygon
import types 

def getCentroid(x):

	if isinstance(x, Point):
		check = type(x)
		print("\nIt is a Shapely: ", check)
		point_cent = x.centroid 
		return point_cent 
	elif isinstance(x, LineString):
		check_line = type(x)
		print("\nIt is a Shapely: ", check_line)
		line_centroid = x.centroid
		return line_centroid 
	elif isinstance(x, Polygon):
		check_poly = type(x)
		print("\nIt is a Shapely: ", check_poly)
		poly_centroid = x.centroid
		return poly_centroid
	else:
		check_rand = type(x)
		print("\nTypeError: This function requires one of Shapely's geometric objects as input.\nNot: ", check_rand)

# creating a Shapely Point - object:
helsinki = Point(60.1, 24.9)
		
# creating a Shapely LineString Object:
point1_line = Point(50.1, 14.9)
point2_line = Point(60.2, 24.8)
point3_line = Point(70.3, 34.7)

line_geom = LineString([point1_line, point2_line, point3_line]) 
		
# creating a Shapely Polygon -object:
hudson_bay = [(63.8, -89.8), (62.5, -77.8), (54.8, -79.0), (58.8, -94.3)]
poly_hudson = Polygon(shell= hudson_bay)

# creating a normal tuple to check the else -argument:
test_list = [(63.8, -89.8), (62.5, -77.8), (54.8, -79.0), (58.8, -94.3)]

# implementing the function on selected variables:
point_test = getCentroid(helsinki)
line_test = getCentroid(line_geom)
poly_test = getCentroid(poly_hudson)
test_list1 = getCentroid(test_list)

# printing out the results: 
print(point_test)
print(line_test)
print(poly_test)
print(test_list1) 

#-------------- Section: 2 -------------------------------------------------------------------

# Create a function called getArea() that takes a Shapely's Polygon -object as input and returns the area of that 
# geometry. Demonstrate the usage of the function. 

# creating a function to calculate the area of Polygon -object: 
def getArea(poly):
	poly_area = poly.area
	return poly_area 

# assigning coordinate-tuples to a variable, rough voordinates for Hudsons bay:	
hudson_bay = Polygon([(63.8, -89.8), (62.5, -77.8), (54.8, -79.0), (58.8, -94.3)])

# implementing the function to a variable: 
hudson_bay_area = getArea(hudson_bay)

# printing out the area of the assigned variable: 
print(hudson_bay_area)


#---------- Section: 3 ---------------------------------------------------------------------------

# Create a function called getLength() takes either a Shapely's LineString or Polygon -object as input. Function should 
# check the type of the input and returns the length of the line if input is LineString and length of the exterior ring if input 
# is Polygon. If something else is passed to the function, it should tell the user --> "Error: LineString or Polygon 
# geometries required!". Demonstrate the usage of the function.

def getLength(x):
	 
	if isinstance(x, Polygon):
		poly_ext = x.exterior 
		poly_len = poly_ext.length
		return poly_len 
	elif isinstance(x, LineString):
		line_length = x.length
		return line_length
	else:
		print("Not a LineString nor a Polygon")

# assigning coordinates to varables that represent points in Mannerheimintie:
point1_mansku = Point(60.1, 24.9)
point2_mansku = Point(60.2, 24.8)
point3_mansku = Point(60.3, 24.7)

# implementing the function by assigning Point objects to the function:	
road_mansku = LineString([point1_mansku, point2_mansku, point3_mansku])

# same drill with Polygon: 
hudson_bay = [(63.8, -89.8), (62.5, -77.8), (54.8, -79.0), (58.8, -94.3)]
poly_hudson = Polygon(shell= hudson_bay)

# Testing that the function can only process LineString and Polygon -objects: 		
test_Poly = getLength(poly_hudson)
test_Line = getLength(road_mansku)
print(test_Poly)
print(test_Line)















