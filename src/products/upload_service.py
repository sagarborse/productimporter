import logging
import csv
from models import Product


class UploadService(object):

    @classmethod
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = logging.getLogger('custom_logger')

    @classmethod
    def save(self):
        with open(self.file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            next(data)
            products = []
            for row in data:
                product = Product(
                    name=row[0],
                    sku=row[1],
                    description=row[2],
                    isactive=1
                )
                products.append(product)
                if len(products) > 5000:
                    Product.objects.bulk_create(products)
                    products = []

            if products:
                Product.objects.bulk_create(products)



