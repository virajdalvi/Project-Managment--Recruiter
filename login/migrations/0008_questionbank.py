# Generated by Django 3.0.5 on 2021-12-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_testscore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=5000)),
                ('optionA', models.CharField(max_length=500)),
                ('optionB', models.CharField(max_length=500)),
                ('optionC', models.CharField(max_length=500)),
                ('optionD', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
    ]
