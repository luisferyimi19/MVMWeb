# Generated by Django 5.0.2 on 2024-04-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_passenger_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='photo',
            field=models.ImageField(blank=True, db_column='photo', help_text='Photo', null=True, upload_to='travel/passengers', verbose_name='Photo'),
        ),
    ]