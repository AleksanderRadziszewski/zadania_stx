# Generated by Django 2.2.6 on 2020-11-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_num',
            field=models.CharField(max_length=20),
        ),
    ]