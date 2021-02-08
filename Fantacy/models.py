from django.db import models

# Create your models here.
class Fantacy(models.Model):
    sr = models.AutoField(primary_key=True)
    slug = models.IntegerField(unique=True)
    title = models.CharField(max_length=500, default='')
    author = models.CharField(max_length=5000, default='')
    thumnail = models.ImageField(upload_to="fantacy")
    content = models.TextField(blank=True)
    publish_date = models.DateField(null=True)
    

    def __str__(self):
        return self.title