# Generated by Django 4.2.11 on 2024-04-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.CharField(max_length=100)),
                ('length', models.FloatField()),
            ],
        ),
    ]
