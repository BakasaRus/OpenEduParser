# Generated by Django 2.2.7 on 2019-11-24 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=8, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Направление подготовки',
                'verbose_name_plural': 'Направления подготовки',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('logo', models.CharField(max_length=255, verbose_name='Логотип')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Организатор',
                'verbose_name_plural': 'Организаторы',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('groups', models.ManyToManyField(to='courses.Group', verbose_name='Направления подготовки')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Organizer', verbose_name='Организатор')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]