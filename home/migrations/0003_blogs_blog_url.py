# Generated by Django 5.0 on 2024-07-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_post_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='blog_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
