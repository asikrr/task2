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

    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='images/')
    status = models.CharField(max_length=1, choices=STATUS, default='n', verbose_name='Статус')
    comment = models.TextField(help_text='Комментарий к заявке', blank=True)
    customer = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    result_image = models.ImageField(blank=True, upload_to='images/')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-date']
        permissions = (("can_change_status", "Смена статуса заявки"),)

    def get_absolute_url(self):
        return reverse('designrequest-detail', args=[str(self.id)])

    def __str__(self):
        return self.title