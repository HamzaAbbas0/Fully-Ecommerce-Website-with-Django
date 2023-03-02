# Generated by Django 4.1.5 on 2023-01-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=110)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=90)),
                ('state', models.CharField(max_length=90)),
                ('zip_code', models.CharField(max_length=90)),
            ],
        ),
    ]
