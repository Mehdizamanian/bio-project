# Generated by Django 3.2 on 2023-08-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('email', models.CharField(max_length=230)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=230)),
                ('birthday', models.CharField(max_length=230)),
                ('website', models.CharField(max_length=230)),
                ('city', models.CharField(max_length=230)),
            ],
        ),
    ]
