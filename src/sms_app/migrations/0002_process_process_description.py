# Generated by Django 3.0.5 on 2020-04-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='process_description',
            field=models.TextField(default='Process description'),
            preserve_default=False,
        ),
    ]
