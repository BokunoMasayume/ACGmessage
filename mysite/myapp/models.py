# coding:utf-8
from django.db import models

# Create your models here.
class iAnimeModel(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=80)
    country = models.CharField(max_length=60)
    year = models.IntegerField()
    season = models.CharField(max_length=6)
    key_word = models.CharField(max_length=80)
    ori_type=models.CharField(max_length=20)
    episode = models.IntegerField()
    state = models.BooleanField(default=True)
    img = models.ImageField(upload_to='Anime')
    summary = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['-year']

class iComicModel(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=40)
    country = models.CharField(max_length=60)
    episode = models.IntegerField()
    key_word = models.CharField(max_length=80)
    company = models.CharField(max_length=60)   
    state = models.BooleanField(default=True)
    year = models.IntegerField()
    img = models.ImageField(upload_to='Comic')
    summary = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['-year'] 


class iBookModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=80)
    publisher = models.CharField(max_length=80)
    key_word = models.CharField(max_length=80)      
    country = models.CharField(max_length=60)
    state = models.BooleanField(default=True)
    volume = models.IntegerField()
    year = models.IntegerField()
    img = models.ImageField(upload_to="Books")
    summary = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['-year']     

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['username'] 

class Comment(models.Model):
    person =  models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['-time'] 