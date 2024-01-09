# Generated by Django 5.0.1 on 2024-01-05 18:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
        ('product', '0002_productimage_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='owner',
            new_name='author',
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('author', 'product')},
        ),
    ]
