from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
        
    def __str__(self):
        return self.name