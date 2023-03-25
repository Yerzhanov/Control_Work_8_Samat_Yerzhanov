from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, default='Other')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание продукта')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, upload_to='products_images', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Продукт: {self.name} | Категория {self.category.name}'


class Review(models.Model):
    RATING_CHOICES = [
        ('0', 'Нет оценки'),
        ('1', 'Не советую'),
        ('2', 'На небольшой бюджет'),
        ('3', 'Можно пользоваться'),
        ('4', 'Лучший выбор'),
        ('5', 'Для мажоров'),
    ]

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, related_name='review')
    product = models.ManyToManyField(to=Product) # Вначале был ForeignKey и все работало прекрасно
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Отзыв')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='0')

    def __str__(self):
        return f'Отзыв для {self.user.username} {self.user.email} ' \
               f'| Продукт {self.product.name} | Оценка {self.rating}'

