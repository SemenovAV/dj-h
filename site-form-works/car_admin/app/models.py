from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name=_('brand'))
    model = models.CharField(max_length=50, verbose_name=_('model'))

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name=_('car'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    text = models.TextField()

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
