from django.db import models
from django.utils import timezone

from profiles.models import User

# Create your models here.
class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Package(models.Model):
    """Model migration design for holidays"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    destination = models.CharField(max_length=150, null=True, blank=True)
    departs = models.CharField(max_length=150, null=True, blank=True)
    length = models.CharField(null=True, blank=True, max_length=50)
    start = models.DateField()
    cover = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, 
                                related_name='comments')
    user = models.ForeignKey(User, null=False, default='', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = (
            'submitted_at',
            )

    def __str__(self):
        return f'Comment by {self.user} on {self.package} at {self.submitted_at}'
