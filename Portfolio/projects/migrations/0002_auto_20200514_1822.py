# Generated by Django 3.0.4 on 2020-05-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('certi_id', models.AutoField(primary_key=True, serialize=False)),
                ('certi_name', models.CharField(max_length=50)),
                ('org', models.CharField(max_length=50)),
                ('issue_date', models.DateField()),
                ('cred_id', models.CharField(max_length=50, null=True)),
                ('cred_url', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='projects',
            name='main_image',
            field=models.ImageField(default='', upload_to='projects/'),
        ),
    ]