# Generated by Django 2.2.28 on 2023-10-27 11:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stregsystem', '0017_auto_20220511_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('desired_amount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='stregsystem.Product')),
            ],
            options={
                'verbose_name_plural': 'Inventory',
            },
        ),
        migrations.CreateModel(
            name='InventoryItemHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_quantity', models.IntegerField(default=0)),
                ('old_quantity', models.IntegerField(default=0)),
                ('count_date', models.DateField(default=django.utils.timezone.now)),
                ('sold_out', models.BooleanField(default=False)),
                ('sold_out_date', models.DateField(blank=True, null=True)),
                ('loss', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item_history', to='stregsystem.InventoryItem')),
            ],
            options={
                'verbose_name_plural': 'Inventory History',
            },
        ),
    ]