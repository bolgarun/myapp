# Generated by Django 2.2.1 on 2019-06-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190610_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(max_length=755),
        ),
    ]
