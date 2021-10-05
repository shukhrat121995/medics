from django.db import models


class MemberOfFls(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.person)


class MemberOfDuodecim(models.Model):
    class Meta:
        ordering = ['-id']

    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.person)
