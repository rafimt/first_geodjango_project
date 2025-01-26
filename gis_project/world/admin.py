from django.contrib import admin
from .models import Incidences, Counties, berlin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    list_display =('name','location')
    
class CountiesAdmin(LeafletGeoAdmin):
    list_display =('counties','codes')
    
class berlinAdmin(LeafletGeoAdmin):
    list_display =('district','pop_density')
    
admin.site.register(Incidences,IncidencesAdmin)
admin.site.register(Counties,CountiesAdmin)
admin.site.register(berlin,berlinAdmin)