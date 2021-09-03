from django.shortcuts import render, get_object_or_404
from .models import Post#, Especie, Mascota

# probando poner_adopcion
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils import timezone

# probando paginacion
from django.core.paginator import Paginator

#formulario
from .forms import EnviarMascota

from django.contrib.auth.models import User

# Create your views here. En la app adopcion
def adopta(request):
    mascota = Post.objects.all()#.order_by('post')
    
    # probando paginacion
    """
    Cambiar a 24 (8 filas en grande y 12 filas en small, 120/24 son 5 paginas constantes)
    hacer que se eliminen registros automaticamente y hacer lo mismo para las otras vistas.
    """
    paginator = Paginator(mascota, 24) # Show 2 mascota per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'adopcion/adopta.html', {'mascota': mascota, 'page_obj': page_obj})




def poner_adopcion(request):
    
    if request.method == 'POST':
        form = EnviarMascota(request.POST, request.FILES) #
        
        if form.is_valid():
            
            
            """ objPost = Post()
            objPost.autor = request.user
            objPost.descripcion = form.cleaned_data['descripcion']
            objPost.contacto = form.cleaned_data['contacto'] """
            
            """ #funciona!
            objPost = Post()
            #post = form.save(commit=False)
            objPost.autor = request.user
            #descripcion = form.cleaned_data['descripcion']
            objPost.descripcion = request.POST.get('descripcion')
            objPost.contacto = request.POST.get('contacto')
            objPost.nombre = request.POST.get('nombre')
            objPost.raza = request.POST.get('raza')
            objPost.medida = request.POST.get('medida')
            objPost.tipo = request.POST.get('especie')
            #fecha_publi = timezone.now()
            objPost.save() """
            

            # ESTO ES LO ULTIMO FUNCIONANDO !!!!!!!!!!!!!!!!!!!
            objPost = Post()

            objPost.autor = request.user
            #descripcion = form.cleaned_data['descripcion']
            objPost.descripcion = form.cleaned_data['descripcion']
            objPost.contacto = form.cleaned_data['contacto']
            objPost.nombre = form.cleaned_data['nombre']
            objPost.raza = form.cleaned_data['raza']
            objPost.medida = form.cleaned_data['medida']
            objPost.tipo = form.cleaned_data['especie']
            objPost.img1 = form.cleaned_data['img1']
            objPost.img2 = form.cleaned_data['img2']
            objPost.img3 = form.cleaned_data['img3']
            
            #objPost.img1 = request.FILES['img1']
            #objPost.img2 = request.FILES['img2']
            #objPost.img3 = request.FILES['img3']
            
            
            #objPost.save()
            
            """ objPost = Post(img1=request.FILES['img1'])
            objPost = Post(img2=request.FILES['img2'])
            objPost = Post(img3=request.FILES['img3']) """
            
            objPost.save()
            
            return HttpResponseRedirect(reverse('adopta') )
    else:
        form = EnviarMascota()
    
    return render(request, 'adopcion/poner_adopcion.html', {'form': form})


def perros(request):
    perros = Post.objects.filter(tipo='perro')#.order_by('post')
    
    #probando paginacion:
    paginator = Paginator(perros, 24) # Show 2 mascota per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'adopcion/perros.html', {'perros': perros, 'page_obj': page_obj})

def gatos(request):
    #gatos = Post.objects.filter(especie__tipo='gato').order_by('post')
    gatos = Post.objects.filter(tipo='gato')
    
    #probando paginacion:
    paginator = Paginator(gatos, 24) # Show 2 mascota per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'adopcion/gatos.html', {'gatos': gatos, 'page_obj': page_obj})

def otros(request):
    #otros = Mascota.objects.filter(especie__tipo='otro').order_by('post')
    otros = Post.objects.filter(tipo='otro')
    
    #probando paginacion:
    paginator = Paginator(otros, 24) # Show 2 mascota per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'adopcion/otros.html', {'otros': otros, 'page_obj': page_obj})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    mascotas = Post.objects.all()
    return render(request, 'adopcion/post_detail.html', {'mascotas': mascotas, 'post': post})

