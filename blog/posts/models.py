from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateTimeField()
    slug = models.SlugField()
    # category = models.ForeignKey('blog.Category')


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
