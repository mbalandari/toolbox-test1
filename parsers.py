from xml.dom import minidom

kml = minidom.parse("time-stamp-point.kml")
PlaceMarks = kml.getElementsByTagName("Placemark")
print(len(PlaceMarks))
