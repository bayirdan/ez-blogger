# Generated by Django 4.1.5 on 2024-04-14 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='categories',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
