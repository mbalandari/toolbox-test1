import geojson

p = geojson.Point([-92, 37])

geojs = geojson.dumps(p, indent=4)
print(geojs)
