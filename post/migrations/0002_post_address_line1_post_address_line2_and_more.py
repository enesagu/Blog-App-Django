# Generated by Django 5.0.3 on 2024-03-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address_line1',
            field=models.CharField(blank=True, max_length=255, verbose_name='Adres Satırı 1'),
        ),
        migrations.AddField(
            model_name='post',
            name='address_line2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Adres Satırı 2'),
        ),
        migrations.AddField(
            model_name='post',
            name='address_type',
            field=models.CharField(choices=[('HM', 'Ev'), ('WK', 'İş'), ('OT', 'Diğer')], default='HM', max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Şehir'),
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ülke'),
        ),
        migrations.AddField(
            model_name='post',
            name='material_type',
            field=models.CharField(choices=[('BR', 'Tuğla'), ('CN', 'Beton'), ('WD', 'Ahşap'), ('ST', 'Çelik'), ('GL', 'Cam')], default='BR', max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='Posta Kodu'),
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(blank=True, max_length=100, verbose_name='Eyalet/Bölge'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Başlık'),
        ),
    ]
