# Generated by Django 3.0.5 on 2020-04-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0004_remove_process_process_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='process_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_name',
            field=models.CharField(max_length=250),
        ),
    ]