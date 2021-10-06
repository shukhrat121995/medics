from django.db import models


class Internship(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.ForeignKey('pages.Person', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    name_of_clinic_or_department = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.person)


class DoctoralDegree(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.ForeignKey('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    field_of_doctorate = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.person)


class Speciality(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.ForeignKey('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)

    name_of_speciality = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.person)


class Docentship(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.ForeignKey('pages.Person', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    name_of_docentship = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.person)


class FirstPublicPost(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)

    date = models.DateField(null=True, blank=True)

    name_of_post = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.person)


class HighestPost(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)

    date = models.DateField(null=True, blank=True)

    name_of_post = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.person)