# Generated by Django 3.2.7 on 2021-09-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
