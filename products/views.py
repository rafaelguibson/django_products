from django.shortcuts import render
from django.http import HttpResponse
# Importar o model para chamar a listagem de produtos
from products.models import Product

# Create your views here.
def products_view(request):
    # Lista Todos os produtos, como uma query select * from produts
    products_list = Product.objects.all()
    return render(
        request=request, 
        template_name='products.html',
        context={'products_list': products_list})