from django.db import models


class User(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    birth_date = models.DateField("Дата рождения", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    localisation = models.CharField('Локализация (язык)')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
