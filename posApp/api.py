import json
from django.http import JsonResponse
from .cart import Cart
from django.shortcuts import get_object_or_404
from .views import *
from .models import *
from .utils import checkout


def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}

    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, updated_quantity=False, quantity=1)
    else:
        cart.add(product=product, updated_quantity=True, quantity=quantity)

    return JsonResponse(jsonresponse)


def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'Success': True}

    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)


def api_checkout(request):
    data = json.loads(request.body)
    cart = Cart(request)
    jsonresponse = {'success': True}

    customer_name = data['customer_name']
    customer_phone = data['customer_phone']
    orderId = checkout(request, customer_name, customer_phone)

    paid = True

    if paid == True:
        order = SellProducts.objects.get(pk=orderId)
        order.paid = True
        order.paid_amount = cart.get_total_cost()

        order.save()
        cart.clear()
        print("Checkout Saved")
    return JsonResponse(jsonresponse)

