# Generated by Django 3.0.1 on 2020-03-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_moodstress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodstress',
            name='id',
        ),
        migrations.AddField(
            model_name='moodstress',
            name='username',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
