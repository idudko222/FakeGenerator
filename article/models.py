from django.db import models


class Article(models.Model):

    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст")
    localisation = models.CharField('Локализация (язык)')
    published_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
