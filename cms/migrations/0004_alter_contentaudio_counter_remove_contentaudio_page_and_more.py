# Generated by Django 4.1.2 on 2022-10-10 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_contentvideo_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentaudio',
            name='counter',
            field=models.IntegerField(default=0, verbose_name='Счетчик просмотров'),
        ),
        migrations.RemoveField(
            model_name='contentaudio',
            name='page',
        ),
        migrations.AlterField(
            model_name='contentaudio',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contenttext',
            name='counter',
            field=models.IntegerField(default=0, verbose_name='Счетчик просмотров'),
        ),
        migrations.RemoveField(
            model_name='contenttext',
            name='page',
        ),
        migrations.AlterField(
            model_name='contenttext',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contentvideo',
            name='counter',
            field=models.IntegerField(default=0, verbose_name='Счетчик просмотров'),
        ),
        migrations.RemoveField(
            model_name='contentvideo',
            name='page',
        ),
        migrations.AlterField(
            model_name='contentvideo',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='contentaudio',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.page'),
        ),
        migrations.AddField(
            model_name='contenttext',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.page'),
        ),
        migrations.AddField(
            model_name='contentvideo',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.page'),
        ),
    ]
