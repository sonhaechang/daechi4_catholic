# Generated by Django 2.1.7 on 2019-12-17 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_school_school_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_class',
            field=models.CharField(choices=[('elementary', '초등부'), ('middlehigh', '중고등부')], db_index=True, max_length=15),
        ),
    ]
