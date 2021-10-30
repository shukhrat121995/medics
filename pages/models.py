from django.db import models
from family.models import Father, Mother, SocialClass


class Person(models.Model):
    class Meta:
        ordering = ['-id']

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    LANGUAGE = [
        ('Finnish', 'Finnish'),
        ('Swedish', 'Swedish')
    ]
    name = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True)
    place_of_birth = models.CharField(max_length=255, blank=True)
    birth = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)

    father = models.ForeignKey(Father, on_delete=models.SET_NULL, blank=True, null=True)
    mother = models.ForeignKey(Mother, on_delete=models.SET_NULL, blank=True, null=True)
    social_class = models.ForeignKey(SocialClass, on_delete=models.SET_NULL, blank=True, null=True)
    language = models.CharField(max_length=7, choices=LANGUAGE, blank=True)

    retirement = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)

    def __str__(self):
        return self.name

