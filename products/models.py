import random
import os

from django.db import models
from django.db.models import Model


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 2541781232)
    name, ext = get_filename_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_name}".format(new_filename=new_filename, final_name=final_name)

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=10.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def ProductListView(self):
        return self.title
