# Generated by Django 5.0 on 2024-04-28 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='crated_at',
            new_name='created_at',
        ),
    ]