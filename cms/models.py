from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Определяем абстрактынй класс для разных типов контента
class Content(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    order = models.IntegerField("Порядок")
    counter = models.IntegerField(
        verbose_name='Счетчик просмотров',
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['order', ]

# Определяем спецефичные поля
class ContentVideo(Content):
    page = models.ForeignKey("Page",verbose_name="Видео", on_delete=models.CASCADE, related_name="content_video")
    url_file = models.URLField("Ссылка на файл")
    url_sub = models.URLField("Ссылка на субтитры")

class ContentAudio(Content):
    page = models.ForeignKey("Page",verbose_name="Аудио", on_delete=models.CASCADE, related_name="content_audio")
    bitrate = models.IntegerField("Битрейт")


class ContentText(Content):
    page = models.ForeignKey("Page", verbose_name="Текст", on_delete=models.CASCADE, related_name="content_text")
    text = models.TextField("Текст")

