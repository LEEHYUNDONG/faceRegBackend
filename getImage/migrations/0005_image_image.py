# Generated by Django 3.2.2 on 2021-05-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getImage', '0004_remove_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='../media/james.jpg', upload_to='face'),
        ),
    ]
