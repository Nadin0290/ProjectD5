# Generated by Django 4.0.2 on 2022-03-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Категория'),
        ),
    ]
