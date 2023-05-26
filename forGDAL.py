from osgeo import gdal

raster = gdal.Open("SatImage.tif")

bands = raster.RasterCount
xPixels = raster.RasterXSize
yPixels = raster.RasterYSize

print(bands, xPixels, yPixels)
