from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Category(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='images/')
    status = models.CharField(max_length=1, choices=STATUS, default='n', help_text='Статус заявки')
    comment = models.TextField(help_text='Комментарий к заявке')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.title