# Generated by Django 4.1.5 on 2024-04-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_categories_blog_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(default=1, to='blog.category'),
        ),
    ]
