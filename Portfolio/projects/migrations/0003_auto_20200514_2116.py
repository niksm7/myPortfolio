# Generated by Django 3.0.4 on 2020-05-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200514_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('msg', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='certifications',
            name='cred_url',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
