# Generated by Django 3.0.6 on 2021-03-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210327_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='details_show',
            field=models.BooleanField(default=False),
        ),
    ]
