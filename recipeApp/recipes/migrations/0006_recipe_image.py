# Generated by Django 5.1.3 on 2024-11-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='https://dummyimage.com/450x300/dee2e6/6c757d.jpg', upload_to='recipes_photos/'),
        ),
    ]
