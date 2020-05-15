from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.CharField(max_length=64, verbose_name='Имя раздела')
    relation = models.ManyToManyField(
        Article,
        through='Relationship',
        through_fields=('scope', 'article', 'main'),
    )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.topic


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Тематика статьи')
    is_main = models.BooleanField(verbose_name='Основной раздел')

    class Meta:
        verbose_name = 'Тема'

    def __str__(self):
        return f'{self.article}_{self.is_main}_{self.scope}'
