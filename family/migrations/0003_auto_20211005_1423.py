# Generated by Django 3.2.7 on 2021-10-05 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='children',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='father',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='mother',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='spouse',
            options={'ordering': ['-id']},
        ),
    ]
