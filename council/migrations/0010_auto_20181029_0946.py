# Generated by Django 2.0.1 on 2018-10-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0009_auto_20181029_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='roll',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]