# Generated by Django 3.0.6 on 2021-03-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_details_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='diseases',
            field=models.TextField(default='empty', null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='diseases_show',
            field=models.TextField(default='empty', null=True),
        ),
    ]
