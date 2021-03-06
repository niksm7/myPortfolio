# Generated by Django 3.0.4 on 2020-05-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200514_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='is_top',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='certifications',
            name='cred_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='certifications',
            name='cred_url',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
