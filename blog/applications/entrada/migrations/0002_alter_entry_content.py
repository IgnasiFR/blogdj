# Generated by Django 5.0.3 on 2024-03-28 12:53

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='contenido'),
        ),
    ]