# Generated by Django 2.2.1 on 2019-06-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_chat_name_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='name_chat',
            field=models.CharField(default=None, max_length=80),
        ),
    ]
