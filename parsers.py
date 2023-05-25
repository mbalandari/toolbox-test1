from xml.dom import minidom

kml = minidom.parse("time-stamp-point.kml")
PlaceMarks = kml.getElementsByTagName("Placemark")
coordinates = PlaceMarks[0].getElementsByTagName("coordinates")
point = coordinates[0].firstChild.data
x, y, z = point.split(",")
x = float(x)
y = float(y)
z = float(z)
print(x, y, z)
