# Generated by Django 3.0.1 on 2020-02-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200201_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_Of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
