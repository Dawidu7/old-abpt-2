# Generated by Django 4.0.3 on 2022-11-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
