# Generated by Django 3.0.3 on 2020-04-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200428_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='demo',
            field=models.CharField(default='0000000', max_length=200),
        ),
    ]