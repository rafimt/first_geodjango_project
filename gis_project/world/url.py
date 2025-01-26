from django.urls import include, path

from . import views

app_name = 'world'

urlpatterns = [
path('',views.homepage, name='home'),
path('county/',views.county_datasets, name='county'),
path('incidence/',views.point_datasets, name='incidence'),
]