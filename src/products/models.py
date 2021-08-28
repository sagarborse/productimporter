from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = 'products'

    name = models.CharField(max_length=256)
    sku = models.CharField(max_length=64)
    description = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return "{} - {}".format(self.name, self.sku)


