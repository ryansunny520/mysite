from django.db import models

class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    # 用户名唯一，unique=True
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Mata:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
