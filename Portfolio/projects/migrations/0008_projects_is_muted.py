# Generated by Django 3.0.4 on 2020-05-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200515_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='is_muted',
            field=models.BooleanField(default=False),
        ),
    ]
