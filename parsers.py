from xml.dom import minidom

kml = minidom.parse("time-stamp-point.kml")
PlaceMarks = kml.getElementsByTagName("Placemark")
coordinates = PlaceMarks[0].getElementsByTagName("coordinates")
point = coordinates[0].firstChild.data
print(point)
