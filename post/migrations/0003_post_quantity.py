# Generated by Django 5.0.3 on 2024-03-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_address_line1_post_address_line2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Price'),
        ),
    ]