from .models import Post#, Especie, Mascota

def ultimosTres(request):
    #ultimosTres = Mascota.objects.all().order_by('post')[:3] #
    
    #ultimosTres = Post.objects.all()[:3]
    if Post.objects.exists():
        ultimosTres = Post.objects.all()[:3]
    else:
        ultimosTres = False
    
    return {'ultimosTres': ultimosTres}