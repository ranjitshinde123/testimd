# Generated by Django 4.1.1 on 2022-09-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_rename_created_at_stock_createdat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
