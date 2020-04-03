from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_date = models.DateTimeField(
        auto_now=False, auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'django2_user'
        verbose_name = "사용자"
        verbose_name_plural = "사용자"

    def __str__(self):
        return self.email
