# Generated by Django 4.1.4 on 2022-12-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='static/food/images/food-placeholder.jpg', max_length=500, upload_to=''),
        ),
    ]
