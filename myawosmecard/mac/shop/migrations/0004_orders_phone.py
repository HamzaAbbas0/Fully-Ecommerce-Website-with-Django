# Generated by Django 4.1.5 on 2023-01-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]
