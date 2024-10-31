from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.price}'