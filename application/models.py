from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model

MIN = validators.MinValueValidator
MAX = validators.MaxValueValidator

User = get_user_model()


class Result(models.Model):
    result = models.FloatField()

    def __str__(self):
        return self.result


class Color(models.Model):
    CHOICES = (("r", "red"), ("g", "green"), ("b", "blue"))

    color = models.CharField(choices=CHOICES, max_length=10)
    number = models.SmallIntegerField(validators=(MIN(1), MAX(100)), help_text="Номер предмета от 1 до 100.")
    user = models.ForeignKey(User, related_name="colors", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        ordering = ("pk",)
        constraints = (models.UniqueConstraint(fields=["number", "user"], name="uniq_item"),)
