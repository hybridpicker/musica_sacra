# Generated by Django 3.2 on 2022-07-07 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_content_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='content_lead',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]