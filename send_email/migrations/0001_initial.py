# Generated by Django 3.0.3 on 2020-04-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('subject', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('to', models.EmailField(max_length=254)),
            ],
        ),
    ]
