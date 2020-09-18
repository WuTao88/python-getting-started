from django.db import models

# Create your models here.
class accounts(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('名字',max_length=64)
    email=models.CharField('邮箱',unique=True,max_length=64)
    password=models.CharField('密码',max_length=64)
    info=models.CharField('个人简介',blank=True,max_length=128)
    create_time=models.DateField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = "用户"    
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
class notes(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(accounts,on_delete=models.CASCADE)
    theme=models.CharField('主题',max_length=100)
    date=models.DateField('创建时间',auto_now_add=True)
    weather=models.CharField('天气',choices=[('sunny','晴'),('cloudy','阴'),('rainy','雨'),('snowy','雪')],max_length=32)
    content=models.CharField('内容',blank=True,max_length=1024)
    create_time=models.DateField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = "日记"    
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.theme

class talkings(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(accounts,on_delete=models.CASCADE)
    content=models.CharField('说说',blank=True,max_length=512)
    pic=models.ImageField('图片', null=True, blank=True, upload_to='static/talking')
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = "说说"    
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content    