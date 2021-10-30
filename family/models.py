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
    date_of_marriage = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Children(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.ForeignKey('pages.Person', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class SocialClass(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Social Class'
        verbose_name_plural = 'Social Classes'

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
