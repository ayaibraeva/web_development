from django.http.request import HttpRequest
from django.http.response import JsonResponse
from core.models import Product

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_Json() for product in products]
    return JsonResponse(products_json, safe=False)



def product_details(request, product_id):
    try:
     product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.to_Json())
