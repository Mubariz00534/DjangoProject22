from django.db import models
import random
import os

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

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
    image = models.ImageField(blank=True, null=True, upload_to=upload_image_path) # pip install pillow

    def __str__(self):
        return self.title