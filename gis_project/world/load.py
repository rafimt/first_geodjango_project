import os
from django.contrib.gis.utils import LayerMapping
from .models import berlin

berlin_mapping = {
    'district': 'district',
    'ew2022': 'ew2022',
    'area': 'area',
    'pop_density': 'pop_density',
    'geom': 'UNKNOWN',
}

berlin_gpkg = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'berlin', 'berlin_district_population.gpkg'))

def run(verbose=True):
    lm = LayerMapping(berlin, berlin_gpkg, berlin_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)
    