# Generated by Django 4.1.4 on 2022-12-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='https://cdn-icons-png.flaticon.com/512/8228/8228779.png', max_length=500, upload_to=''),
        ),
    ]