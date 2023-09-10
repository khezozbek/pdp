from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    img = models.ImageField(upload_to='menu-img', blank=False, null=False)
    text = models.TextField(max_length=1400)

