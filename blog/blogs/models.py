from os import name
from django.db import models
from datetime import date
from django.urls import reverse
from django.core.validators import MinLengthValidator

from django.db.models.deletion import SET_NULL



# Create your models here.

class Author(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.First_Name}"

class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Excerpt = models.CharField(max_length=100)
    Slug = models.SlugField(max_length=100,unique=True,db_index=True)
    Date = models.DateField(auto_now=True)
    Image = models.FileField(upload_to="postimages",null=True)
    Content = models.TextField(validators=[MinLengthValidator(10)])
    Author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="post",null=True)
    Tag = models.ManyToManyField(Tag,related_name="post")

    def get_absolute_url(self):
        return reverse("indpost", args=[self.Slug])

    def __str__(self):
        return f"{self.Title}"


class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name


class Picture(models.Model):
    pic = models.FileField(upload_to="images")
