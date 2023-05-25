import geojson
from shapely.geometry import shape

p = geojson.Point([-92, 37])
geojs = geojson.dumps(p, indent=4)
point = shape(p)
print(point.wkt)
