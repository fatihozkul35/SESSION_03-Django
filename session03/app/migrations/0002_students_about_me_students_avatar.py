# Generated by Django 4.0.4 on 2022-04-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='about_me',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='avatar',
            field=models.ImageField(default=123, upload_to=''),
            preserve_default=False,
        ),
    ]
