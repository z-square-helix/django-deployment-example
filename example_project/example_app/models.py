from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):

    top_name = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):

    topic = models.ForeignKey(Topic, on_delete = models.PROTECT)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):

    name = models.ForeignKey(Webpage, on_delete = models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Userinos(models.Model):

    first_name = models.CharField(max_length = 132)
    last_name = models.CharField(max_length = 132)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.first_name

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete = models.PROTECT)

    # additional
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username
