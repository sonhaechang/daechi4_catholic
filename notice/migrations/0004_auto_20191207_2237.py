# Generated by Django 2.0.7 on 2019-12-07 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='notice',
            new_name='post',
        ),
    ]
