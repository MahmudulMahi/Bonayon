# Generated by Django 3.0.6 on 2021-03-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_product_details_details_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='details',
            field=models.TextField(default='empty', null=True),
        ),
    ]