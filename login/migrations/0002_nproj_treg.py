# Generated by Django 3.1.1 on 2020-10-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nproj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('sem', models.CharField(max_length=100)),
                ('rno', models.IntegerField(max_length=5)),
                ('pname', models.CharField(max_length=100)),
                ('subj', models.CharField(max_length=100)),
                ('tuser', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('pmem', models.CharField(max_length=200)),
                ('filename', models.ImageField(upload_to='output')),
            ],
        ),
        migrations.CreateModel(
            name='Treg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
