# Generated by Django 4.2.11 on 2024-04-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='nothing', max_length=1000),
        ),
    ]
