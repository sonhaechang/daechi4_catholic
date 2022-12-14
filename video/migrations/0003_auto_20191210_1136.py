# Generated by Django 2.0.7 on 2019-12-10 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0002_auto_20191118_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='video.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='video',
        ),
        migrations.DeleteModel(
            name='VideoComment',
        ),
    ]
