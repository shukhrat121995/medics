from django.db import models


class Father(models.Model):
    class Meta:
        ordering = ['-id']
    name = models.CharField(max_length=255, unique=True)
    occupation = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Mother(models.Model):
    class Meta:
        ordering = ['-id']
    name = models.CharField(max_length=255, unique=True)
    maiden_name = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Spouse(models.Model):
    class Meta:
        ordering = ['-id']
    person = models.ForeignKey('pages.Person', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    occupation = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Children(models.Model):
    class Meta:
        ordering = ['-id']
    person = models.ForeignKey('pages.Person', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name