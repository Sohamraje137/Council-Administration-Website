# Generated by Django 2.1.1 on 2018-09-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('council', '0002_auto_20180917_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='roll',
            field=models.CharField(default='16co216', max_length=8, unique=True),
            preserve_default=False,
        ),
    ]