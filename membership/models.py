from django.db import models


class MemberOfFls(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Member of FLS'
        
    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.person)


class MemberOfDuodecim(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Member of Duodecim'

    person = models.OneToOneField('pages.Person', on_delete=models.CASCADE)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.person)
