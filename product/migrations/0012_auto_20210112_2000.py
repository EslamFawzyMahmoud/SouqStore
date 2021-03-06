# Generated by Django 3.1.4 on 2021-01-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_prdslug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PRDcost',
            new_name='PRDCost',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PRDcreated',
            new_name='PRDCreated',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PRDname',
            new_name='PRDName',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PRDprice',
            new_name='PRDPrice',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDDiscountPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Discount Price'),
            preserve_default=False,
        ),
    ]
