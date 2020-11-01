# Generated by Django 3.1.2 on 2020-10-29 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('isbn_num', models.CharField(max_length=13)),
                ('pages_amount', models.IntegerField()),
                ('link', models.URLField(max_length=128)),
                ('pub_language', models.CharField(max_length=30)),
            ],
        ),
    ]
