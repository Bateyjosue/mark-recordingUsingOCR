# Generated by Django 3.2.10 on 2022-06-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_enroll_module_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll',
            name='booklet',
            field=models.IntegerField(default=0),
        ),
    ]