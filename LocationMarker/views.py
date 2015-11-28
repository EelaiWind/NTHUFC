from django.shortcuts import render,  HttpResponseRedirect
from .models import Marker, DemoPhoto
from django.core.urlresolvers import reverse
from random import randrange

# Create your views here.
def editMarker (request):
	context = { 'markerList':Marker.objects.all()};
	return render(request,'LocationMarker/editMarker.html', context);

def post (request):
	
	titleList = request.POST.getlist('title');
	latList = request.POST.getlist('lat');
	lngList = request.POST.getlist('lng');
	if len(titleList) > 0:
		Marker.objects.all().delete();
	for i in range(len(titleList)):
		Marker.objects.create(title=titleList[i], latitude=latList[i], longitude=lngList[i]);

	context = {'pack':Marker.objects.all()};
	return  HttpResponseRedirect(reverse('LocationMarker:editMarker'));

def demo(request):
	url = 'https://farm6.staticflickr.com/5776/22094071913_a6f5c32200_z.jpg';
	DemoPhoto.objects.all().delete();
	markers = Marker.objects.order_by('?');
	for i in range(int(len(markers)*0.8)):
		DemoPhoto.objects.create(title='photo_{}'.format(i), url=url, marker=markers[i]);
	
	context = {'photoList':DemoPhoto.objects.all()};
	return  render(request, 'LocationMarker/demo.html',context);