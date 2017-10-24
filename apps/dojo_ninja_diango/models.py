from __future__ import unicode_literals
from django.db import models
# Create your models here.

class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    def __repr__(self):
        return "dojos: ---,{} ----{}, ----{}".format(self.name, self.city, self.state)
    

class ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(dojos, related_name="nin")
    def __repr__(self):
        return "ninjas: ---,{} ----{}".format(self.first_name, self.last_name)

# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.

# class Dojo(models.Model):
#     name = models.CharField(max_length = 255)
#     city = models.CharField(max_length = 255)
#     state = models.CharField(max_length = 2)
#     def __repr__(self):
#         return "Dojo:\n{}\n{}\n{}".format(self.name, self.city, self.state)

# class Ninja(models.Model):
#     first_name = models.CharField(max_length = 255)
#     last_name = models.CharField(max_length = 255)
#     desc = models.TextField()
#     dojo = models.ForeignKey(Dojo, related_name = "ninjas")
#     def __repr__(self):
#         return "Ninja:\n{}\n{}\n{}".format(self.first_name, self.last_name, self.dojo)

