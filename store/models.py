from django.db import models
from django.urls import reverse
from category.models import Category
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    previous_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)
    images = models.ImageField(upload_to='media/products/')
    stock = models.PositiveIntegerField()
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)    
    created_date = models.DateTimeField(auto_now=True) 
    modified_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name