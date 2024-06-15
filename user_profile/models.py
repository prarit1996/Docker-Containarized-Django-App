from django.db import models

# Create your models here.
class UserProfile(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  profile_desc = models.CharField(max_length=100)
  profile_tags = models.CharField(max_length=100)