# Generated by Django 4.2.1 on 2023-06-01 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_categories_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
