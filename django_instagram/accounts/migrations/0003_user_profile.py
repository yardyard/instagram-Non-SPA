# Generated by Django 3.0.14 on 2022-02-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220208_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, upload_to='accounts/proflie/%Y/%m/%d'),
        ),
    ]
