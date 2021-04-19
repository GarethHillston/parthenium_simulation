import matplotlib.pyplot as plt
import geopandas as gp

filePath0 = './data/pak_admbnda_adm0_ocha_pco_gaul_20181218.shp'
filePath1 = './data/pak_admbnda_adm1_ocha_pco_gaul_20181218.shp'
filePath2 = './data/pak_admbnda_adm2_ocha_pco_gaul_20181218.shp'
filePath3 = './data/pak_admbnda_adm3_ocha_pco_gaul_20181218.shp'
filePathAll = './data/pak_admbndl_admALL_ocha_pco_gaul_itos_20181218.shp'

levelZeroDF = gp.read_file(filePath0)
levelOneDF = gp.read_file(filePath1)
levelTwoDF = gp.read_file(filePath2)
levelThreeDF = gp.read_file(filePath3)
levelAllDF = gp.read_file(filePathAll)

plottingDF = levelThreeDF

#plottingDF.to_crs()
plottingDF['area'] = plottingDF.area
plottingDF.to_crs('crs')
plottingDF.plot('area', cmap='OrRd', scheme='fisher_jenks')
plt.show()
