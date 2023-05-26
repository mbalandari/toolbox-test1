import rasterio

ds = rasterio.open("SatImage.tif")

print(ds.name, ds.count, ds.width, ds.height)
