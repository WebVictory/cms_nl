# Generated by Django 4.1.2 on 2022-10-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ContentVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('order', models.IntegerField(max_length=30)),
                ('counter', models.IntegerField(max_length=30)),
                ('page', models.ManyToManyField(to='cms.page')),
            ],
        ),
        migrations.CreateModel(
            name='ContentText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('order', models.IntegerField(max_length=30)),
                ('counter', models.IntegerField(max_length=30)),
                ('page', models.ManyToManyField(to='cms.page')),
            ],
        ),
        migrations.CreateModel(
            name='ContentAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('order', models.IntegerField(max_length=30)),
                ('counter', models.IntegerField(max_length=30)),
                ('page', models.ManyToManyField(to='cms.page')),
            ],
        ),
    ]