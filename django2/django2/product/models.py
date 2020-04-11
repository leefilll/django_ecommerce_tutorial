from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    registered_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'django2_product'
        verbose_name = "제품"
        verbose_name_plural = "제품"

    def __str__(self):
        return self.name
