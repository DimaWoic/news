# Generated by Django 2.2 on 2020-06-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20200603_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='cloudiness',
            field=models.IntegerField(verbose_name='облачность'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='precipitation',
            field=models.IntegerField(verbose_name='осадки'),
        ),
    ]