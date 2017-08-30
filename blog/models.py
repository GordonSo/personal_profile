from django.db import models

# Create your models here.


class Blogger(models.Model):

    created_date = models.DateTimeField(verbose_name="created date")
    creator_id = models.TextField(verbose_name="creator id")
    FirstName = models.CharField(verbose_name="first name", max_length=100)
    LastName = models.CharField(verbose_name="last name", max_length=100)
    content = models.TextField(verbose_name="content")


class Blog(models.Model):

    created_date = models.DateTimeField(verbose_name="created date")
    creator = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="title", max_length=1000)
    content = models.TextField(verbose_name="content")
