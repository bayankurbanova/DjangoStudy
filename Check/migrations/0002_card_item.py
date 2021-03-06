# Generated by Django 3.1.3 on 2020-12-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_id', models.IntegerField(verbose_name='Айди владельца')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование товара')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('card_id', models.IntegerField(verbose_name='Айди товара')),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='avatar')),
            ],
        ),
    ]
