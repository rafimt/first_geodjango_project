from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties, Incidences
# from django.views.generic import TemplateView
# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'index.html'
    
def homepage(request):
    # return HttpResponse("Hello World! I am home")
    return render(request, 'index.html')

def county_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')