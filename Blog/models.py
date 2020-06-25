from django.db import models

class BlogModel(models.Model):
    id = models.AutoField(primary_key=True)
    blogTitle = models.CharField(max_length=300)
    blogImage = models.ImageField(upload_to='images/')
    blogDescription = models.TextField()
    blogBody = models.TextField()
    uplaodBy= models.CharField(max_length=30)
    publishDate = models.DateTimeField()
