# Generated by Django 4.1.2 on 2022-12-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zenmind', '0002_rename_title_post_flag_rename_author_post_item_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Title', max_length=100),
            preserve_default=False,
        ),
    ]
