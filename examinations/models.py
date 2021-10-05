from django.db import models


class Matriculation(models.Model):
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class Premedical(models.Model):
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class CandidateOfPhilosophy(models.Model):
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class CandidateOfMedicine(models.Model):
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class LicentiateOfPhilosophy(models.Model):
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class Dispensation(models.Model):
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class Legislation(models.Model):
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)
