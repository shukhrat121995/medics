from django.db import models


class Matriculation(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Matriculation'
        verbose_name_plural = 'Matriculation'
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class Premedical(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Premedical'
        verbose_name_plural = 'Premedical'
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class CandidateOfPhilosophy(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Candidate of Philosophy'
        verbose_name_plural = 'Candidate of Philosophy'
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class CandidateOfMedicine(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Candidate of Medicine'
        verbose_name_plural = 'Candidate of Medicine'
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class LicentiateOfPhilosophy(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Licentiate of Medicine'
        verbose_name_plural = 'Licentiate of Medicine'
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class Dispensation(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Dispensation (women only)'
        verbose_name_plural = 'Dispensation (women only)'
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)


class Legislation(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = 'Legislation'
        verbose_name_plural = 'Legislation'
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=255, blank=True)
    grade = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person)
