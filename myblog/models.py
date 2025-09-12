from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    #content = models.TextField()
    newcontent = RichTextField(config_name='default',max_length=300000,blank=True)
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=150)
    timeStamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title
