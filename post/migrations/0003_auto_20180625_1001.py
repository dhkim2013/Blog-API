# Generated by Django 2.0.6 on 2018-06-25 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20180621_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='post.Tag'),
        ),
    ]
