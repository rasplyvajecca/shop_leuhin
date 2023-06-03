from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)
    CHOICE_GROUP = {
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Children', 'Children')
    }
    category = models.CharField('Категория', max_length=255, choices=CHOICE_GROUP)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.FloatField('Цена')
    image = models.ImageField('Фото', upload_to='product/products/')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Message(models.Model):
    email = models.CharField('Почта', max_length=50)
    message = models.TextField('Комментарий')
    created_at = models.DateTimeField('Время создания', auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'