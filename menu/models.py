from django.db import models
from cloudinary import models as modelCloudinary
# Create your models here.
class Plato(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=45, null=False)
  # https://support.cloudinary.com/hc/en-us/community/posts/360005466760-How-do-I-change-the-upload-path-for-image-in-Cloudinary
  foto = modelCloudinary.CloudinaryField(folder='plato') # models.ImageField()
  disponible = models.BooleanField(default=True, null=False)
  precio = models.FloatField( null=False)

  class Meta:
    db_table='platos'
    