# Generated by Django 4.1.2 on 2022-12-03 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zenmind', '0003_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='item_owner',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='item_url',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='date_posted',
        ),
        migrations.RemoveField(
            model_name='post',
            name='flag',
        ),
    ]
