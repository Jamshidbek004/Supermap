from django.db import models

# Create your models here.
from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from audioop import reverse

from django.db import models
from django.utils import timezone

from django.urls import reverse

# Create your models here.
class Category(models.Model):
    nomi=models.CharField(max_length=250)
    def __str__(self):
        return self.nomi
#
# class News(models.Model):
#     class Status(models.TextChoices):
#         qoralama = "QR","qoralama"
#         chopetilish = "CHP", "chopetilish"
#
#     nom = models.CharField(max_length=1000)
#     slug = models.SlugField(max_length=250)
#     kontent = models.TextField()
#     rasm = models.ImageField(upload_to='news/images')
#     filelar = models.FileField(upload_to='news/fayllar')
#     chopetilishVaqti = models.DateTimeField(default=timezone.now)
#     yaratilganVaqti =models.DateTimeField(auto_now_add=True)
#     ozgarishVaqti = models.DateTimeField(auto_now=True)
#     holati =models.CharField(max_length=3,choices=Status.choices,default=Status.qoralama)
#
#     kategory = models.ForeignKey(Category,on_delete=models.CASCADE)
#     views = models.IntegerField(default=0)
#     comentlarsoni = models.IntegerField()
#     qaynoq_yangiliklar = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['-chopetilishVaqti']
#     objects = models.Manager()
#
#     def __str__(self):
#         return self.nom
#
# class yangilik_video(models.Model):
#     nom = models.CharField(max_length=111)
#     video = models.FileField(upload_to='yangi/fayllar', null=True, verbose_name="")
#     comentlarsoni = models.IntegerField()
#     views= models.IntegerField(default=0)
#     chopetilishVaqti = models.DateTimeField(default=timezone.now)
#
#     class Meta:
#         ordering = ['-chopetilishVaqti']
#
#     objects = models.Manager()
# class yangilikDetel(models.Model):
#     nom = models.CharField(max_length=500)
#     text = models.TextField()
#     text1 = models.TextField()
#     text2= models.TextField()
#     rasm = models.ImageField(upload_to='news/images')
#     rasm1 = models.ImageField(upload_to='news/images')
#     rasm2 = models.ImageField(upload_to='news/images')
#     chopetilishVaqti = models.DateTimeField(default=timezone.now)
#
#     class Meta:
#         ordering = ['-chopetilishVaqti']
#
# class Comments(models.Model):
#     news = models.ForeignKey(News,
#                              on_delete=models.CASCADE,
#                              related_name="comments")
#     user = models.ForeignKey(User,
#                              on_delete=models.CASCADE,
#                              related_name="comments")
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)
#
#     class Mete :
#         ordering = ["created_at"]
#     def __str__(self):
#         return f"Comments: {self.body} by {self.user}"

class SongiYangiliklar(models.Model):
    class Status(models.TextChoices):
        qoralama = "QR","qoralama"
        chopetilish = "CHP", "chopetilish"

    nom = models.CharField(max_length=10001)
    slug = models.SlugField(max_length=10001)
    kontent = models.TextField()
    rasm = models.ImageField(upload_to='news/images')
    chopetilishVaqti = models.DateTimeField(default=timezone.now)
    yaratilganVaqti =models.DateTimeField(auto_now_add=True)
    ozgarishVaqti = models.DateTimeField(auto_now=True)
    holati =models.CharField(max_length=3,choices=Status.choices,default=Status.qoralama)
    kategory = models.ForeignKey(Category,on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-chopetilishVaqti']
    objects = models.Manager()

    def __str__(self):
        return self.nom
class Voqealar(models.Model):
    class Status(models.TextChoices):
        qoralama = "QR","qoralama"
        chopetilish = "CHP", "chopetilish"

    nom = models.CharField(max_length=10001)
    slug = models.SlugField(max_length=10001)
    kontent = models.TextField()
    video = models.FileField(upload_to='yangi/fayllar')
    rasm = models.ImageField(upload_to='news/images')
    chopetilishVaqti = models.DateTimeField(default=timezone.now)
    yaratilganVaqti =models.DateTimeField(auto_now_add=True)
    ozgarishVaqti = models.DateTimeField(auto_now=True)
    holati =models.CharField(max_length=3,choices=Status.choices,default=Status.qoralama)
    kategory = models.ForeignKey(Category,on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-chopetilishVaqti']
    objects = models.Manager()

    def __str__(self):
        return self.nom




