# Generated by Django 5.0.3 on 2024-03-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='address_line1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='address_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
        migrations.RemoveField(
            model_name='post',
            name='country',
        ),
        migrations.RemoveField(
            model_name='post',
            name='material_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='post',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='post',
            name='state',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(verbose_name='Yayımlanma Tarihi'),
        ),
    ]