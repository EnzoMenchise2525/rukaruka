from django import forms


################## logueo de iniciar_sesion.html ###############

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model  # Importa get_user_model

class Inicio_Sesion(AuthenticationForm):
    class Meta:
        model = get_user_model()  # Utiliza get_user_model()
        fields = ['username', 'password']


################## Editar informacion ###############

from django import forms
from .models import Usuario

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'cargo', 'telefono', 'fecha_de_nacimiento', 'direccion', 'foto_de_perfil', 'imagen_de_fondo']
        
        
########################  admin_agregar_intSocial.html #####################################  

from django import forms
from .models import Social, Social_imagen1, Social_imagen2, Social_imagen3, Social_imagen4

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['imagen_social', 'titulo_social', 'fecha_social', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_social', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class SocialImagen1Form(forms.ModelForm):
    class Meta:
        model = Social_imagen1
        fields = ['imagen']

class SocialImagen2Form(forms.ModelForm):
    class Meta:
        model = Social_imagen2
        fields = ['imagen']

class SocialImagen3Form(forms.ModelForm):
    class Meta:
        model = Social_imagen3
        fields = ['imagen']

class SocialImagen4Form(forms.ModelForm):
    class Meta:
        model = Social_imagen4
        fields = ['imagen']
        
########################  admin_agregar_energetico.html #####################################  

from django import forms
from .models import Energetico, Energetico_imagen1, Energetico_imagen2, Energetico_imagen3, Energetico_imagen4

class EnergeticoForm(forms.ModelForm):
    class Meta:
        model = Energetico
        fields = ['imagen_energetico', 'titulo_energetico', 'fecha_energetico', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_energetico', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class EnergeticoImagen1Form(forms.ModelForm):
    class Meta:
        model = Energetico_imagen1
        fields = ['imagen']

class EnergeticoImagen2Form(forms.ModelForm):
    class Meta:
        model = Energetico_imagen2
        fields = ['imagen']

class EnergeticoImagen3Form(forms.ModelForm):
    class Meta:
        model = Energetico_imagen3
        fields = ['imagen']

class EnergeticoImagen4Form(forms.ModelForm):
    class Meta:
        model = Energetico_imagen4
        fields = ['imagen']

########################  admin_agregar_vivienda.html #####################################  

from django import forms
from .models import Vivienda, Vivienda_imagen1, Vivienda_imagen2, Vivienda_imagen3, Vivienda_imagen4

class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = ['imagen_vivienda', 'titulo_vivienda', 'fecha_vivienda', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_vivienda', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class ViviendaImagen1Form(forms.ModelForm):
    class Meta:
        model = Vivienda_imagen1
        fields = ['imagen']

class ViviendaImagen2Form(forms.ModelForm):
    class Meta:
        model = Vivienda_imagen2
        fields = ['imagen']

class ViviendaImagen3Form(forms.ModelForm):
    class Meta:
        model = Vivienda_imagen3
        fields = ['imagen']

class ViviendaImagen4Form(forms.ModelForm):
    class Meta:
        model = Vivienda_imagen4
        fields = ['imagen']



########################  admin_agregar_reconstruccion.html #####################################  

from django import forms
from .models import Reconstruccion, Reconstruccion_imagen1, Reconstruccion_imagen2, Reconstruccion_imagen3, Reconstruccion_imagen4

class ReconstruccionForm(forms.ModelForm):
    class Meta:
        model = Reconstruccion
        fields = ['imagen_reconstruccion', 'titulo_reconstruccion', 'fecha_reconstruccion', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_reconstruccion', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class ReconstruccionImagen1Form(forms.ModelForm):
    class Meta:
        model = Reconstruccion_imagen1
        fields = ['imagen']

class ReconstruccionImagen2Form(forms.ModelForm):
    class Meta:
        model = Reconstruccion_imagen2
        fields = ['imagen']

class ReconstruccionImagen3Form(forms.ModelForm):
    class Meta:
        model = Reconstruccion_imagen3
        fields = ['imagen']

class ReconstruccionImagen4Form(forms.ModelForm):
    class Meta:
        model = Reconstruccion_imagen4
        fields = ['imagen']


########################  admin_agregar_areasVerdes.html #####################################  

from django import forms
from .models import Verdes, Verdes_imagen1, Verdes_imagen2, Verdes_imagen3, Verdes_imagen4

class VerdesForm(forms.ModelForm):
    class Meta:
        model = Verdes
        fields = ['imagen_verdes', 'titulo_verdes', 'fecha_verdes', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_verdes', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class VerdesImagen1Form(forms.ModelForm):
    class Meta:
        model = Verdes_imagen1
        fields = ['imagen']

class VerdesImagen2Form(forms.ModelForm):
    class Meta:
        model = Verdes_imagen2
        fields = ['imagen']

class VerdesImagen3Form(forms.ModelForm):
    class Meta:
        model = Verdes_imagen3
        fields = ['imagen']

class VerdesImagen4Form(forms.ModelForm):
    class Meta:
        model = Verdes_imagen4
        fields = ['imagen']

########################  admin_agregar_Condominio.html #####################################  

from django import forms
from .models import Condominio, Condominio_imagen1, Condominio_imagen2, Condominio_imagen3, Condominio_imagen4

class CondominioForm(forms.ModelForm):
    class Meta:
        model = Condominio
        fields = ['imagen_condominio', 'titulo_condominio', 'fecha_condominio', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_condominio', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class CondominioImagen1Form(forms.ModelForm):
    class Meta:
        model = Condominio_imagen1
        fields = ['imagen']

class CondominioImagen2Form(forms.ModelForm):
    class Meta:
        model = Condominio_imagen2
        fields = ['imagen']

class CondominioImagen3Form(forms.ModelForm):
    class Meta:
        model = Condominio_imagen3
        fields = ['imagen']

class CondominioImagen4Form(forms.ModelForm):
    class Meta:
        model = Condominio_imagen4
        fields = ['imagen']



########################  admin_agregar_Asbesto.html #####################################  

from django import forms
from .models import Asbesto, Asbesto_imagen1, Asbesto_imagen2, Asbesto_imagen3, Asbesto_imagen4

class AsbestoForm(forms.ModelForm):
    class Meta:
        model = Asbesto
        fields = ['imagen_asbesto', 'titulo_asbesto', 'fecha_asbesto', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_asbesto', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class AsbestoImagen1Form(forms.ModelForm):
    class Meta:
        model = Asbesto_imagen1
        fields = ['imagen']

class AsbestoImagen2Form(forms.ModelForm):
    class Meta:
        model = Asbesto_imagen2
        fields = ['imagen']

class AsbestoImagen3Form(forms.ModelForm):
    class Meta:
        model = Asbesto_imagen3
        fields = ['imagen']

class AsbestoImagen4Form(forms.ModelForm):
    class Meta:
        model = Asbesto_imagen4
        fields = ['imagen']
        
########################  admin_agregar_comunitaria.html #####################################  

from django import forms
from .models import Comunitaria, Comunitaria_imagen1, Comunitaria_imagen2, Comunitaria_imagen3, Comunitaria_imagen4

class ComunitariaForm(forms.ModelForm):
    class Meta:
        model = Comunitaria
        fields = ['imagen_comunitaria', 'titulo_comunitaria', 'fecha_comunitaria', 'servicio', 'nombre_ciudad', 'nombre_tipo_servicio', 'texto_comunitaria', 'imagen1', 'imagen2', 'imagen3', 'imagen4']

class ComunitariaImagen1Form(forms.ModelForm):
    class Meta:
        model = Comunitaria_imagen1
        fields = ['imagen']

class ComunitariaImagen2Form(forms.ModelForm):
    class Meta:
        model = Comunitaria_imagen2
        fields = ['imagen']

class ComunitariaImagen3Form(forms.ModelForm):
    class Meta:
        model = Comunitaria_imagen3
        fields = ['imagen']

class ComunitariaImagen4Form(forms.ModelForm):
    class Meta:
        model = Comunitaria_imagen4
        fields = ['imagen']
        
########################  recuperar_contrasenna.html #####################################  


class RecuperarContrasenaForm(forms.Form):
    correo = forms.EmailField()
    
    
########################  agregar_ubicacion.html ##################################### 
import json
from django import forms
from .models import Ubicacion

# Carga el JSON con codificación UTF-8
with open('principal/static/chile.json', encoding='utf-8') as json_file:
    CHILE_JSON = json.load(json_file)

from django import forms
from .models import Ubicacion

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre_lugar', 'ciudad', 'comuna', 'latitud', 'longitud']

    def __init__(self, *args, **kwargs):
        super(UbicacionForm, self).__init__(*args, **kwargs)

        # Obtén las ciudades desde la base de datos
        ciudades = Ubicacion.objects.values_list('ciudad', flat=True).distinct()

        # Establece las opciones para el campo de ciudad
        self.fields['ciudad'].choices = [('','')] + [(ciudad, ciudad) for ciudad in ciudades]

        # Establece las opciones para el campo de comuna (inicialmente vacío)
        self.fields['comuna'].choices = [('','')]

        # Añadir un atributo de clase para la actualización dinámica de opciones
        self.fields['comuna'].widget.attrs['class'] = 'comuna-dropdown'

        # Agregar un script de inicialización para las opciones dinámicas
        self.fields['comuna'].widget.attrs['onchange'] = 'actualizar_comunas();'

