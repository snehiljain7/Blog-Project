from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 400)
    description = models.CharField(max_length = 400)
    image = models.FileField(upload_to = 'images/')
    author = models.CharField(max_length=50, default = '')
    upload_date = models.DateTimeField(auto_now = True)
