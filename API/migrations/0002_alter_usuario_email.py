# Generated by Django 3.2.5 on 2022-01-31 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
