# Generated by Django 2.2.9 on 2020-02-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200225_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question1',
            field=models.CharField(choices=[('I', 'Introvert'), ('E', 'Extrovert')], default='I', max_length=1),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question2',
            field=models.CharField(choices=[('S', 'Sensing'), ('N', 'intutive')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question3',
            field=models.CharField(choices=[('T', 'Thinkimg'), ('F', 'Feeling')], default='T', max_length=1),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question4',
            field=models.CharField(choices=[('J', 'Judging'), ('P', 'perceivimg')], default='P', max_length=1),
        ),
    ]
