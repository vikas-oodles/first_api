# Generated by Django 2.2.5 on 2020-07-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200731_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]
