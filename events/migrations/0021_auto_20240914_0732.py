# Generated by Django 3.2 on 2024-09-14 07:32

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20240513_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('date', 'time'), 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='events/images/', verbose_name='Beitragsbild (Ratio: 16:9)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_thumb',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='events/images/', verbose_name='Event Thumbnail (Ratio 1:1)'),
        ),
    ]
