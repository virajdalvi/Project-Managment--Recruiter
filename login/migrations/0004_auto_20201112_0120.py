# Generated by Django 3.1.1 on 2020-11-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20201020_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('suggestions', models.TextField()),
                ('avgtotal', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='nproj',
            name='filename',
        ),
        migrations.AddField(
            model_name='nproj',
            name='file',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nproj',
            name='pid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='nproj',
            name='rno',
            field=models.IntegerField(),
        ),
    ]
