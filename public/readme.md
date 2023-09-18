# Australian Exclusive Economic Zone AMB 2020 - Clipped to Tropics (AIMS, GA)
This dataset corresponds to the Australian Maritime Boundaries Exclusive Economic Zone clipped to the tropics, i.e. only retaining the boundary above the [Tropic of Capricorn](https://en.wikipedia.org/wiki/Tropic_of_Capricorn) at -23.43621 deg latitude.

Full details of this dataset can be found at https://github.com/eatlas/AU_GA_AMB2020_EEZ-Limit_Tropics

# Attribution

- **Title:** Australian Exclusive Economic Zone AMB 2020 - Clipped to Tropics (AIMS, GA)
- **Processing:** Eric Lawrey, Australian Institute of Marine Science
- **License:** Creative Commons Attribution 4.0 International Licence http://creativecommons.org/licenses/
- **Creation date:** 19 September 2023

# Source data

## EEZ and Territorial sea - AMB
Alcock, M.B., Taffs, N.J., Zhong, Q. 2020. Seas and Submerged Lands Act 1973 - Australian Maritime Boundaries 2020 - Geodatabase. Geoscience Australia, Canberra. https://pid.geoscience.gov.au/dataset/ga/144571

Creative Commons Attribution 4.0 International Licence http://creativecommons.org/licenses/

## GEODATA COAST 100K 2004
2004. GEODATA COAST 100K 2004. Geoscience Australia, Canberra. https://pid.geoscience.gov.au/dataset/ga/61395

Creative Commons Attribution 4.0 International Licence http://creativecommons.org/licenses/

# Processing

The outer line feature of the EEZ (EEZ Limits) was converted it to a polygon. It was then clipped to a bounding box of the tropics (AU_GA_AMB2020_EEZ-Limit_No-land-clip_Tropics.shp). A second derivative was made by clipping out the Australian Mainland (AU_GA_AMB2020_EEZ-Limit_Tropics.shp). Processing was performed in QGIS. 