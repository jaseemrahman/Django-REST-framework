# Generated by Django 4.0.5 on 2022-07-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronicdevicedetail',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='uploads'),
        ),
    ]
