# Generated by Django 3.1.1 on 2021-03-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='uses',
            field=models.TextField(default='empty', null=True),
        ),
    ]
