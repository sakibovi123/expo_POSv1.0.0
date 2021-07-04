from .models import SellItems, SellProducts
from .cart import Cart



def checkout(request, customer_name, customer_phone):
    order = SellProducts(customer_name=customer_name, customer_phone=customer_phone)

    order.save()

    cart = Cart(request)

    for item in cart:
        order = SellItems.objects.create(order=order, product=item['product'], buying_price=item['buying_price'], quantity=item['quantity'])

    return order.id