from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from promociones.models import Promocion


def home(request):
    param = request.GET.get('param')
    #promo = Promocion.objects.all()

    print(param)
    promo = Promocion.objects.filter(tipo = param)
    context = {
        'lista_promocion': promo #[:2]
    }

    print(context)



    return render(request, 'promociones/home.html',context)


def detalle(request, pk):

    #try:
    #     promo = Promocion.objects.filter(pk=pk)
    #except Promocion.DoesNotExsist:
    #   promo= None
    #except Promocion.MultipleObjects:
    #    promo = None

    posible_promo = Promocion.objects.filter(pk=pk)

    promo = posible_promo[0] if len(posible_promo) ==1 else None

    if promo is not None:
        #cargo plantilla detalle
        context = {
            'promo': posible_promo  # [:2]
        }

        return render(request, 'promociones/detail.html', context)

    else:
        #response 404
        return HttpResponseNotFound('No existe la promocion')



def banner(request):
    banner = Promocion.objects.filter(banner = True)
    context = {
        'lista_banner': banner #[:2]
    }

    print(context)



    return render(request, 'promociones/banner.html',context)