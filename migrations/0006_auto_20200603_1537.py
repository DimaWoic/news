# Generated by Django 2.2 on 2020-06-03 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200529_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weather',
            options={'ordering': ['published'], 'verbose_name': 'погода'},
        ),
    ]
