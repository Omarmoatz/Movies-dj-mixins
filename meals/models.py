from django.db import models
from django.utils import timezone

class Meal(models.Model):
    name = models.CharField( max_length=100, default='default_meal')
    description = models.TextField( max_length=1000, default='default_desc',blank=True, null=True)
    price = models.DecimalField( max_digits=6, decimal_places=2, default=99.99)
    category = models.ForeignKey('Category', related_name='ctg_meal', on_delete=models.CASCADE,blank=True, null=True)
    preperation_time = models.TimeField( default=timezone.now)
    image = models.ImageField( upload_to='meals/',blank=True, null=True)
    people = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"

    def __str__(self):
        return self.name
    
    @property
    def get_avg_time(self):
        return self.price 

class Category(models.Model):
    name = models.CharField( max_length=100, default='default_ctg')
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


