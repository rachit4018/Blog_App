# Generated by Django 5.0.4 on 2024-04-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
