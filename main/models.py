from django.db import models
from main.models_folder.base import *

class Info(models.Model):

    key = models.CharField(max_length=100, null=False, blank=False, help_text="Ключ настройки", verbose_name="Ключ")
    value = models.CharField(max_length=100, null=True, blank=False, help_text="Значение настройки", verbose_name="Значение")

    def __str__(self):
        return f"'{self.key}' - '{self.value}'"

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информации"

class Positions(Name):

    def __str__(self):
        return f"'{self.name}'"

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

class Mentors(Image):

    fullname = models.CharField(max_length=255, null=False, blank=False, help_text="Фамилия имя преподавателя", verbose_name="ФИО")
    nomer = models.CharField(max_length=255, null=True, blank=False, verbose_name="Номер")
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, verbose_name="Должность")

    def __str__(self):
        return f"'{self.fullname}'"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

class Events(Name, SmallDescription, Image):

    def __str__(self):
        return f"'{self.name}'"

    class Meta:
        verbose_name = "События"
        verbose_name_plural = "События"

class Courses(Name, SmallDescription, Image):

    def __str__(self):
        return f"'{self.name}'"

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"

class Gallery(Image):

    def __str__(self):
        return f"'{self.image.name}'"

    class Meta:
        verbose_name = "Галарея"
        verbose_name_plural = "Галарея"

class News(Name, Image, BigDescription):

    def __str__(self):
        return f"'{self.name}'"

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

