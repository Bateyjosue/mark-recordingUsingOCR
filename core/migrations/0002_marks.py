# Generated by Django 3.2.10 on 2022-05-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_reg_number', models.CharField(max_length=50)),
                ('mark', models.IntegerField()),
                ('add', models.DateTimeField(auto_now=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
