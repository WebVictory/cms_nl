# Generated by Django 4.1.2 on 2022-10-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_alter_contentaudio_page_alter_contenttext_page_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contentaudio',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='contenttext',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='contentvideo',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='contentaudio',
            name='bitrate',
            field=models.IntegerField(default=0, verbose_name='Битрейт'),
        ),
        migrations.AddField(
            model_name='contenttext',
            name='text',
            field=models.TextField(default='', verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='contentvideo',
            name='url_file',
            field=models.URLField(default='www', verbose_name='Ссылка на файл'),
        ),
        migrations.AddField(
            model_name='contentvideo',
            name='url_sub',
            field=models.URLField(default='www', verbose_name='Ссылка на субтитры'),
        ),
        migrations.AlterField(
            model_name='contentaudio',
            name='order',
            field=models.IntegerField(verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='contentaudio',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='contenttext',
            name='order',
            field=models.IntegerField(verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='contenttext',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='contentvideo',
            name='order',
            field=models.IntegerField(verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='contentvideo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
