from shapely import wkt, geometry

wktPoly = "POLYGON((0 0,4 0,4 4,0 4,0 0))"
poly = wkt.loads(wktPoly)
buf = poly.buffer(5.0)
print(poly.area)
print(buf.area)
print(buf.difference(poly).area)
