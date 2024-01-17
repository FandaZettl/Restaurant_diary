from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    cuisine_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name
