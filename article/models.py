from django.db import models


class Article(models.Model):
    POLITICS = 'Политика'
    TECH = 'Технологии'
    BUSINESS = 'Бизнес'

    TAG_CHOICES = [
        (POLITICS, 'Политика'),
        (TECH, 'Технологии'),
        (BUSINESS, 'Бизнес'),
    ]

    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст")
    tag = models.CharField("Тег", max_length=20, choices=TAG_CHOICES, null=True)
    localisation = models.CharField('Локализация (язык)')
    published_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.author})"
