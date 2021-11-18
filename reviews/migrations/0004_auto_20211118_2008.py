# Generated by Django 3.2.8 on 2021-11-18 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=80, unique=True),
        ),
    ]
