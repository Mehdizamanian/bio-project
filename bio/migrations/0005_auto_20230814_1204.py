# Generated by Django 3.2 on 2023-08-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='loc_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='home',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
