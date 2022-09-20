# Generated by Django 2.0.7 on 2022-08-30 12:03

from django.db import migrations, models
import information.models.jumbotron_image


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_auto_20220801_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='JumbotronImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('INTRODUCE', '본당소개'), ('GROUP', '본당단체'), ('NOTICE', '본당소식'), ('PARTICIPATE', '참여마당'), ('SIGNUP', '약관동의/회원가입'), ('LOGIN', '로그인'), ('MYPAGE', '마이페이지'), ('PASSWORD', '비밀번호 찾기/비밀번호 변경'), ('SEARCH', '통합검색')], max_length=11, verbose_name='위치')),
                ('image', models.ImageField(blank=True, null=True, upload_to=information.models.jumbotron_image.jumbotron_image_upload_to, verbose_name='이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '점보트론 이미지',
                'verbose_name_plural': '점보트론 이미지',
            },
        ),
    ]
