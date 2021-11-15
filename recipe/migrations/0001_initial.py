# Generated by Django 3.2.9 on 2021-11-16 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ingredients', models.CharField(max_length=200)),
                ('recipe', models.TextField()),
                ('disease', models.TextField()),
            ],
        ),
    ]
