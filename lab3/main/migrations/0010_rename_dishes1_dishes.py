# Generated by Django 4.0.4 on 2022-05-30 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_categories_dishes1_delete_dishes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dishes1',
            new_name='Dishes',
        ),
    ]
