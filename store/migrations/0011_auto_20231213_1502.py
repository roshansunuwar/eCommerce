# Generated by Django 3.2 on 2023-12-13 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20231213_1443'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kurtha',
        ),
        migrations.DeleteModel(
            name='Pant',
        ),
        migrations.DeleteModel(
            name='Saree',
        ),
        migrations.DeleteModel(
            name='T_Shirt',
        ),
    ]