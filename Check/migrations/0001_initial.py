# Generated by Django 3.1.3 on 2020-11-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True, unique=True, verbose_name='Username')),
                ('email', models.CharField(max_length=35, unique=True, verbose_name='email')),
                ('pas', models.CharField(max_length=50, verbose_name='Password')),
                ('pas1', models.CharField(max_length=50, verbose_name='Password1')),
            ],
        ),
    ]
