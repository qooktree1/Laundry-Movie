# Generated by Django 3.2.12 on 2022-05-25 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]