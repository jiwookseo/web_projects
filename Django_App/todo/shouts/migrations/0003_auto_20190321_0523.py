# Generated by Django 2.1.7 on 2019-03-21 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shouts', '0002_shout_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shout',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
