# Generated by Django 3.2 on 2023-12-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_kurtha'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='t-shirt/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='kurtha',
            name='image',
            field=models.ImageField(upload_to='kurtha/'),
        ),
    ]