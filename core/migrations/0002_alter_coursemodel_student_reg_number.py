# Generated by Django 4.0.3 on 2022-03-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='student_reg_number',
            field=models.CharField(max_length=50),
        ),
    ]
