# Generated by Django 4.1.7 on 2023-02-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('map_url', models.CharField(max_length=240)),
                ('img_url', models.CharField(max_length=240)),
                ('location', models.CharField(max_length=120)),
                ('has_sockets', models.BooleanField(default=False)),
                ('has_toilet', models.BooleanField(default=False)),
                ('has_wifi', models.BooleanField(default=False)),
                ('can_take_calls', models.BooleanField(default=False)),
                ('seats', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coffee_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]