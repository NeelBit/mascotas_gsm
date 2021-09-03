from django.shortcuts import render

from adopcion.models import Post
#from django.http import HttpResponse

# vistas de proyectoWebApp.
def home(request):
    
    #ultima = Post.objects.latest('fecha_publi')
    if Post.objects.exists():
        ultima = Post.objects.latest('fecha_publi')
    else:
        ultima = False
    
    
    return render(request, "mascotasgsmApp/home.html", {'ultimoPost':ultima})

# error 404
from django.http import Http404, HttpResponseNotFound

def mi_error_404(request, post_id):
    
    try:
        p = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("La mascota no se encontró")
    
    return render(request, 'adopcion/404.html', {'p': p})
