from django.db import models


class Hello(models.Model):
    firstname = models.CharField(max_length= 225)
    lasttname = models.CharField(max_length= 225)