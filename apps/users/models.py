from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    gender_choices = (
        ('male','男'),
        ('female','女'),
    )
    nick_name = models.CharField(max_length=50,verbose_name="昵称")
    birday = models.DateField(blank=True,null=True,verbose_name="生日")
    gender = models.CharField(max_length=6,choices=gender_choices,default='female',verbose_name="性别")
    address = models.CharField(max_length=100,verbose_name='地址')
    mobile = models.CharField(max_length=11,verbose_name="手机号码")
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=100)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class EmailVerifyRecord(models.Model):
    send_type_choices = (
        ('register','注册'),
        ('forget','找回密码'),
    )
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField(max_length=10,choices=send_type_choices,verbose_name='验证码类型')
    send_time = models.DateTimeField(auto_now_add=True,verbose_name='发送时间')
    def __str__(self):
        return '%s<%s>' % (self.code,self.email)
    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m',max_length=100,verbose_name="轮播图")
    url = models.URLField(max_length=200,verbose_name="访问地址")
    index = models.PositiveSmallIntegerField(default=100,verbose_name='顺序')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name