# Generated by Django 3.1.4 on 2021-01-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20201231_0317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PRDdesc',
            new_name='PRDDesc',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image'),
        ),
    ]
