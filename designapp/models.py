from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category-list')

    def __str__(self):
        return self.title

class DesignRequest(models.Model):
    STATUS = (
        ('n', 'Новая'),
        ('w', 'Принято в работу'),
        ('d', 'Выполнено'),
    )

    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(default='default.jpg', upload_to='images/', verbose_name='Изображение')
    status = models.CharField(max_length=1, choices=STATUS, default='n', verbose_name='Статус заявки')
    comment = models.TextField(help_text='Комментарий к заявке', blank=True, verbose_name='Комментарий')
    customer = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
    result_image = models.ImageField(blank=True, upload_to='images/', verbose_name='Результат')


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('designrequest-detail', args=[str(self.id)])

    def __str__(self):
        return self.title