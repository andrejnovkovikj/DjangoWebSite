# Generated by Django 4.2.4 on 2023-08-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_card_expirationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expirationDate',
            field=models.CharField(max_length=5),
        ),
    ]
