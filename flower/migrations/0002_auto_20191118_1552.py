# Generated by Django 2.1 on 2019-11-18 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flower',
            options={'ordering': ['-created_at']},
        ),
    ]
