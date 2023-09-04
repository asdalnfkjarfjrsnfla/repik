from django.db import models


class Articles(models.Model):
    objects = None
    title = models.CharField("название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("Статия")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"