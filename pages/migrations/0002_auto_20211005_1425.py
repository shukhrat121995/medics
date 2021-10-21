# Generated by Django 3.2.7 on 2021-10-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='person',
            name='member_of_FLS',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='member_of_duodecim',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]