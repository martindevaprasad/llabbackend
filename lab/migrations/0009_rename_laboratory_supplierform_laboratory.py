# Generated by Django 4.2.3 on 2023-07-09 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_alter_supplierform_certificate_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplierform',
            old_name='Laboratory',
            new_name='laboratory',
        ),
    ]