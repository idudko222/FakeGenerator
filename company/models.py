from django.db import models


class Company(models.Model):
    IT = 'ИТ'
    FINANCE = 'Финансы'
    EDUCATION = 'образование'
    OTHER = 'Другое'

    SECTOR_CHOICES = [
        (IT, 'Информационные технологии'),
        (FINANCE, 'Финансы'),
        (EDUCATION, 'Образование'),
        (OTHER, 'Другое'),
    ]

    name = models.CharField("Название", max_length=100)
    sector = models.CharField("Сфера", max_length=20, choices=SECTOR_CHOICES, null=True)
    inn = models.CharField("ИНН", max_length=12, unique=True)  # 12 цифр для ИНН юрлиц
    founded_date = models.DateField("Дата основания", null=True, blank=True)
    localisation = models.CharField('Локализация (язык)')
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sector})"
