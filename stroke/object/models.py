from django.db import models
from django.urls import reverse


class Object(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Возможные направления'
        verbose_name_plural = 'Возможные направления'
        ordering = ['title', 'time_create']


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Приоритет')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Целевой приоритет'
        verbose_name_plural = 'Целевые приоритеты'
        ordering = ['id']