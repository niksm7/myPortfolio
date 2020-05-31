# Generated by Django 3.0.4 on 2020-05-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200515_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='main_about',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='proj_video',
            field=models.FileField(blank=True, default='', null=True, upload_to='projects/', verbose_name='Video(OPTIONAL)'),
        ),
    ]