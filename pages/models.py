from django.db import models


class Person(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True)

    def __str__(self):
        return self.name
