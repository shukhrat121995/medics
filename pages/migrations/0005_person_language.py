# Generated by Django 3.2.7 on 2021-09-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210924_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='language',
            field=models.CharField(blank=True, choices=[('Finnish', 'Finnish'), ('Swedish', 'Swedish')], max_length=7),
        ),
    ]
