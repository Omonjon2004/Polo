from celery import shared_task
from apps.product.models import Bags, Shoes, Dress, Jewelry


@shared_task
def update_stock(product_type, product_id, quantity):
    if product_type == 'bag':
        product = Bags.objects.get(id=product_id)
    elif product_type == 'shoes':
        product = Shoes.objects.get(id=product_id)
    elif product_type == 'dress':
        product = Dress.objects.get(id=product_id)
    elif product_type == 'jewelry':
        product = Jewelry.objects.get(id=product_id)

    if product:
        product.stock -= quantity  # Zaxiradan kerakli miqdorda kamaytiramiz
        product.save()
