# Generated by Django 5.0.2 on 2024-04-02 06:38

import django_better_admin_arrayfield.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='inclusions',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500, null=True), blank=True, db_column='inclusions', default=list, help_text='Inclusions', size=10, verbose_name='Inclusions'),
        ),
    ]
