# Generated by Django 2.0.7 on 2019-12-10 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flower', '0002_auto_20191118_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='flower.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.Flower')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flower_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='flowercomment',
            name='flower',
        ),
        migrations.RemoveField(
            model_name='flowercomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='flowercomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='FlowerComment',
        ),
    ]
