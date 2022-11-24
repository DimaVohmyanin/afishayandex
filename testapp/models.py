from django.db import models

# Create your models here.


class Place(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название места')
    title_article = models.TextField(max_length=200, verbose_name='Короткое описание')
    text_article = models.TextField(verbose_name='Полное описание места')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'