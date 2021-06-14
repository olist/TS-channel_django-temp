# Generated by Django 3.2.4 on 2021-06-14 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_catalog_id', models.IntegerField(default=0)),
                ('seller_id', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('marketplace', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posted_products', to='channels.marketplace')),
            ],
            options={
                'db_table': 'ProductPost',
                'managed': True,
            },
        ),
    ]
