from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name = "ninjas")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)





#practiced the following questions: 
# Start a new app (the name of the app should be 'dojo_ninjas')
# Create appropriate tables/models that allows you to perform tasks such as
# Dojo.objects.first().ninjas.all()
# Ninja.objects.first().dojo

# Using Django Shell:
#DOJO:
# Have it include the name of the dojo and the city and state of each dojo
# Have the first dojo be "CodingDojo Silicon Valley" in "Mountain View", "CA".
# Have the second dojo be "CodingDojo Seattle" in "Seattle", "WA".
# Have the third dojo be "CodingDojo New York" in "New York", "NY".
# Create 3 dojos
# Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
# Create 3 additional dojos by using Dojo.objects.create
# Create 3 ninjas that belong to the first dojo you created.
# Create 3 more ninjas and have them belong to the second dojo you created. *******
# Create 3 more ninjas and have them belong to the third dojo you created.
# Be able to retrieve all ninjas that belong to the first Dojo
# Be able to retrieve all ninjas that belong to the last Dojo
# Add a new field in the Dojo class (found in your models.py) called 'desc'. Allow 'desc' to hold long text (more than 255 characters). To forward engineer the change, run the appropriate migration commands. Successfully run the migration files and check the records to make sure the new field was added successfully.
