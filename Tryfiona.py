import fiona
from pprint import pprint

f = fiona.open("GIS_CensusTract_poly.shp")
f.driver
print(f.crs)
print(f.bounds)
pprint(f.schema)
print(len(f))
