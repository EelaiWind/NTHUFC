from django.db import models

# Create your models here.
class Marker(models.Model):
	title = models.CharField(max_length=30);
	latitude = models.DecimalField(max_digits=18, decimal_places=15);
	longitude = models.DecimalField(max_digits=18, decimal_places=15);
	def __str__ (self):
		return self.title;

class DemoPhoto(models.Model):
	url = models.CharField(max_length=100);
	title = models.CharField(max_length=30);
	marker = models.ForeignKey('Marker');
	def __str__ (self):
		return self.title;