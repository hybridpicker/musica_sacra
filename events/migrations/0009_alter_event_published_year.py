# Generated by Django 3.2 on 2022-07-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='published_year',
            field=models.IntegerField(default=2022, verbose_name='Year of Article'),
        ),
    ]