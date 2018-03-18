from django.shortcuts import render

# Create your views here.
from primera.models import Presentacion

from promociones.models import Promocion


def prin(request):
    #pre = Presentacion.objects.all()
    pre = Presentacion.objects.filter()
    context = {
        'lispre': pre  # [:2]
    }
    print(context)

    return render(request, 'primera/principal.html', context)


