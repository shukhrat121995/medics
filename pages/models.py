from django.db import models


class Person(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True)
    birth = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)

    def __str__(self):
        return self.name
