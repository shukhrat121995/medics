# Generated by Django 3.2.8 on 2021-10-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0004_children_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='spouse',
            name='date_of_marriage',
            field=models.DateField(blank=True, null=True),
        ),
    ]
