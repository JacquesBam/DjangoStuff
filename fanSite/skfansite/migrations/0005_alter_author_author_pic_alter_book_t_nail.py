# Generated by Django 5.1.1 on 2024-09-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skfansite', '0004_alter_book_t_nail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_pic',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='t_nail',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to=''),
        ),
    ]