from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_visited = models.DateField()
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()
    reting = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.restaurant.name} - {self.date_visited}"
