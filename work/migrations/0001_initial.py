# Generated by Django 3.1 on 2020-09-17 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='名字')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('info', models.CharField(blank=True, max_length=128, verbose_name='个人简介')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='talkings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=512, verbose_name='内容')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='static/talking', verbose_name='图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.accounts')),
            ],
            options={
                'verbose_name': '说说',
                'verbose_name_plural': '说说',
            },
        ),
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('theme', models.CharField(max_length=100, verbose_name='主题')),
                ('date', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('weather', models.CharField(choices=[('sunny', '晴'), ('cloudy', '阴'), ('rainy', '雨'), ('snowy', '雪')], max_length=32, verbose_name='天气')),
                ('content', models.CharField(blank=True, max_length=1024, verbose_name='内容')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.accounts')),
            ],
            options={
                'verbose_name': '日记',
                'verbose_name_plural': '日记',
            },
        ),
    ]
