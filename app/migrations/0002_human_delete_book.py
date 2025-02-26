# Generated by Django 5.0.3 on 2024-11-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('roles', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
