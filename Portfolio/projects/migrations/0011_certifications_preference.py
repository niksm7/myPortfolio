# Generated by Django 3.0.4 on 2020-05-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20200521_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='certifications',
            name='preference',
            field=models.IntegerField(default=100),
        ),
    ]
