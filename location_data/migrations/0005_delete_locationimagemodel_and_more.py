# Generated by Django 4.2.1 on 2023-06-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_data', '0004_remove_location_event_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LocationImageModel',
        ),
        migrations.RemoveField(
            model_name='district',
            name='district_images',
        ),
        migrations.DeleteModel(
            name='DistrictImageModel',
        ),
        migrations.AddField(
            model_name='district',
            name='district_images',
            field=models.FileField(default=0, upload_to='static/uploads'),
            preserve_default=False,
        ),
    ]
