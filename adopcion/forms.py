from django import forms
#from .models import Mascota, Post


class EnviarMascota(forms.Form):
    nombre = forms.CharField(max_length=20, help_text='Si es que ya tiene nombre. Sino deje en blanco', required=False, label='Nombre')
    raza = forms.CharField(max_length=20, help_text='Solo escribe si conoces la raza. Sino deje en blanco',label='Raza', required=False)
    
    MEDIDAS = (
        ('otro', 'No se'),
        ('chico', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),

    )
    medida = forms.ChoiceField(choices=MEDIDAS, help_text='Que tamaño tiene?', required=False) #default=MEDIDAS[3][0] # default='otro'
    #medida = forms.ChoiceField(choices=MEDIDAS, help_text='Que tamaño tiene?', required=False, widget=forms.Select(), initial='No se') #attrs={'disabled':'disabled'}
    
    #medida = forms.CharField(max_length=20, help_text='Que tamaño tiene?', required=False)
    
    """ medida = forms.CharField(
        label='Que medida tiene?',
        max_length=20,
        widget=forms.Select(choices=MEDIDAS),
        help_text='Que tamaño tiene?', 
        required=False,
        #initial='No se',
    ) """
    
    #medida = forms.ChoiceField(choices=MEDIDAS, required=False, help_text='Que tamaño tiene?', label='Que medida tiene?',initial='No se')
    
    
    ESPECIES = (
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otro', 'Otro'),
    )
    especie = forms.ChoiceField(choices=ESPECIES, help_text='Seleccione si es un Perro, Gato, u otra especie', required=True)
    
    #especie = forms.CharField(label='Es un Perro, Gato, u otra especie?' , max_length=20, required=False, help_text='perro / gato / otro')
    
    descripcion = forms.CharField(widget=forms.Textarea, help_text='Por favor sea lo mayormente descriptivo, hasta 1000 caracteres.', max_length=1000, label='Descripción')
    
    img1 = forms.ImageField(label='1ª foto', help_text='Suba la 1º imagen de la mascota', required=True)
    img2 = forms.ImageField(label='2ª foto', help_text='Suba la 2º imagen de la mascota', required=True)
    img3 = forms.ImageField(label='3ª foto', help_text='Suba una 3ª imagen de la mascota', required=True)
    
    
    contacto = forms.CharField(max_length=200, help_text='Coloque las formas de contacto, por favor verifique bien. límite 200 caracteres', label='Contacto')