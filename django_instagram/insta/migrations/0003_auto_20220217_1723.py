# Generated by Django 3.0.14 on 2022-02-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20220214_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='insta/post/%Y%m%d'),
        ),
    ]
