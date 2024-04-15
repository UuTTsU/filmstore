from django.db import models

class Film(models.Model):
    film_name = models.CharField(max_length=100)
    release_date = models.DateField()
    plot = models.TextField(max_length=100)







