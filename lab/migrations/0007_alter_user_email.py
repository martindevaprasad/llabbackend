# Generated by Django 4.2.3 on 2023-07-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]