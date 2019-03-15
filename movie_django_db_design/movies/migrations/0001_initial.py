# Generated by Django 2.1.7 on 2019-03-15 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('audience', models.IntegerField(default=0)),
                ('poster_url', models.CharField(default='', max_length=140)),
                ('description', models.TextField(default='')),
                ('genre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=140)),
                ('score', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
    ]
