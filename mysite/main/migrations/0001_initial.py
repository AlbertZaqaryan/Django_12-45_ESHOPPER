# Generated by Django 4.1.7 on 2023-03-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=60, verbose_name='SliderActive name1')),
                ('name2', models.CharField(max_length=60, verbose_name='SliderActive name2')),
                ('text', models.TextField(verbose_name='SliderActive text')),
                ('img', models.ImageField(upload_to='images', verbose_name='SliderActive image')),
                ('logo', models.ImageField(upload_to='images', verbose_name='SliderActive logo')),
            ],
        ),
    ]
