from django.db import models

class Fruit(models.Model):
    class PriceType(models.TextChoices):
        USD = "USD", "$"
        EURO = 'EURO', '€'

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/fruits/')
    information = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=20, choices=PriceType.choices,default=PriceType.USD)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]

class Vegetable(models.Model):
    class PriceType(models.TextChoices):
        USD = "USD", "$"
        EURO = 'EURO', '€'

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/vegetables/')
    information = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=20, choices=PriceType.choices,default=PriceType.USD)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]




class BestSell(models.Model):
    class PriceType(models.TextChoices):
        USD = "USD", "$"
        EURO = 'EURO', '€'

    title = models.CharField(max_length=50)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to='shop/bestselling/')
    price = models.FloatField()
    price_type = models.CharField(max_length=20, choices=PriceType.choices,default=PriceType.USD)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id']),
        ]