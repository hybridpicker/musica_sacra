# Generated by Django 3.2 on 2024-05-13 16:34

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_alter_event_program_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_thumb',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='events/images/', verbose_name='Beitragsbild Thumbnail'),
        ),
        migrations.AlterField(
            model_name='event',
            name='published_year',
            field=models.IntegerField(default=2024, verbose_name='Jahr der Veranstaltung'),
        ),
    ]
