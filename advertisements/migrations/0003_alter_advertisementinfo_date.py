# Generated by Django 4.0.4 on 2022-04-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_alter_advertisementinfo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementinfo',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
