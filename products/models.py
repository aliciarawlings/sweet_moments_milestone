from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    flavour = models.CharField(max_length=250)    
    
    def __str__(self):
        return self.flavour


class Products(models.Model):
    class Meta:
        verbose_name_plural = "Products"
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    
    QUANTITY_CHOICES = [
        ('500g', 0.5),
        ('1kg', 1),
        ('1.5kg', 1.5),
        ('2kg', 2),
    ]
    
    product = models.ForeignKey('Products', null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(choices=QUANTITY_CHOICES, default=0.5, decimal_places=2, max_digits=6)
  
