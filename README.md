# tips about installing GDAL

- python version 3.11
- GDAL version 3.8.4

- GDAL Wheel download link:
https://github.com/cgohlke/geospatial-wheels/releases

use 
`pip install "gdal file location"`

in settings.py

`if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']`

`GDAL_LIBRARY_PATH = r'C:\Users\rmtum\OneDrive\Desktop\gis_project\.venv\Lib\site-packages\osgeo\gdal.dll'
GEOS_LIBRARY_PATH = r'C:\Users\rmtum\OneDrive\Desktop\gis_project\.venv\Lib\site-packages\osgeo\geos_c.dll'`
