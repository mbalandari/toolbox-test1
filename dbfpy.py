from dbfpy3 import dbf

db = dbf.Dbf("GIS_CensusTract_poly.dbf")
print(db[0])
