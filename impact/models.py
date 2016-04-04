from django.db import models
from django.core.validators import RegexValidator
import warnings
warnings.filterwarnings("ignore", "Field 'subbranch_title' doesn't have a default value")

# Create your models here.
class gallery_image(models.Model):
	image = models.ImageField(upload_to="Images/gallery/")
	image_title = models.CharField(max_length=300,default="Image Title")

	def __unicode__(self):              
        	return self.image_title

class contactus(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	phone_no = models.IntegerField(blank=True)
	message = models.TextField(max_length=5000)

	def __unicode__(self):              
        	return str(self.fname) 
