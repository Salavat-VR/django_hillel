# Generated by Django 3.1.7 on 2021-04-08 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210404_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='subs_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='subs name'),
            preserve_default=False,
        ),
    ]
