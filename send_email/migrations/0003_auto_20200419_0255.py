# Generated by Django 3.0.5 on 2020-04-18 21:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0002_auto_20200419_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
