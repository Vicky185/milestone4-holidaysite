# Generated by Django 3.0.8 on 2020-08-23 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_comment_approved_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
