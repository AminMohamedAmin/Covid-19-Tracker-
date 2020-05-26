from django.db import models

# Create your models here.


class news(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    puplish = models.DateField()

    class Meta:
        ordering = ('-puplish',)
        verbose_name = "New"
        verbose_name_plural = "News"


class advices(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    puplish = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('-puplish',)
        verbose_name = "Advice"
        verbose_name_plural = "Advices"

class questions(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    puplish = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('-puplish',)
        verbose_name = "question"
        verbose_name_plural = "questions"


class Contacts(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    puplish = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('-puplish',)
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"