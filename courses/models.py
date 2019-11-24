from django.db import models


class Organizer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    logo = models.CharField(max_length=255, verbose_name='Логотип')
    url = models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=8, verbose_name='Код')
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'{self.code} {self.name}'

    class Meta:
        verbose_name = 'Направление подготовки'
        verbose_name_plural = 'Направления подготовки'


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='Ссылка')
    groups = models.ManyToManyField(Group, verbose_name='Направления подготовки')
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, verbose_name='Организатор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
