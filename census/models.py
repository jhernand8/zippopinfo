from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

# Census data information type. Contains the key used by the
# census api and a description of the data for that key.
class InfoType(models.Model):
    census_key = models.TextField()
    info_type_id = models.AutoField(primary_key = True)
    description = models.TextField()

# Data for actual census data for a given zip code.
class CensusInfo(models.Model):
    info_type_id = models.IntegerField()
    census_info_id = models.AutoField(primary_key = True)
    info = models.IntegerField()
    zipCode = models.TextField()
    state_code = models.IntegerField()

