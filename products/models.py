from django.db import models
import random
import os
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

# plt.jpg

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)

    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(0, 31232132)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)

    return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename
    )

# https://docs.djangoproject.com/en/3.0/topics/db/managers/
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().featured()
    
    def active(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
    image = models.ImageField(blank=True, null=True, upload_to=upload_image_path) # pip install pillow
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# save() signalini tutmaq ucundur.
pre_save.connect(product_pre_save_receiver, sender=Product)