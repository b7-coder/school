from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Имя")
    class Meta:
        abstract=True

class Image(models.Model):
    image = models.ImageField()
    class Meta:
        abstract=True

class SmallDescription(models.Model):
    description = models.CharField(max_length=100, null=True, blank=False, help_text="Короткое описание", verbose_name="Описание")
    class Meta:
        abstract=True

class BigDescription(models.Model):
    description = models.CharField(max_length=255, null=True, blank=False, help_text="Длинное описание", verbose_name="Описание")
    class Meta:
        abstract=True