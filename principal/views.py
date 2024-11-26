from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def integracion_social(request):
    return render(request, "integracion_social.html")

def nuestra_mision(request):
    return render(request, "nuestra_mision.html")

def iniciar_sesion(request):
    return render(request, "iniciar_sesion.html")

def olvidar_contrasenna(request):
    return render(request, "olvidar_contrasenna.html")

def error_404(request):
    return render(request, "error_404.html")


###################################################################################################
###################################################################################################

###################################################################################################
##########---------------------  ver Noticias  ----------------------- ###############

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.template.loader import render_to_string

##########---------------------  Crear agregar_intSocial  ----------------------- ###############

from django.shortcuts import render, redirect
from .forms import SocialForm, SocialImagen1Form, SocialImagen2Form, SocialImagen3Form, SocialImagen4Form
from .models import Social, Social_imagen1, Social_imagen2, Social_imagen3, Social_imagen4
from django.contrib.auth.decorators import login_required

@login_required
def admin_agregar_intSocial(request):
    social_form = SocialForm()
    social_imagen_form = SocialImagen1Form()

    context = {'social_form': social_form, 'social_imagen_form': social_imagen_form}
    return render(request, 'admin_agregar_intSocial.html', context)

@login_required
def publicar_agregar_intSocial(request):
    if request.method == 'POST':
        social_form = SocialForm(request.POST, request.FILES)
        social_imagen_forms = [SocialImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if social_form.is_valid() and all(social_imagen_form.is_valid() for social_imagen_form in social_imagen_forms):
            social = social_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, social_imagen_form in enumerate(social_imagen_forms, start=1):
                imagen = social_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Social_imagen{i}'](social=social, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_intSocial')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'social_form': social_form, 'social_imagen_forms': social_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_intSocial.html', context)

    return admin_agregar_intSocial(request)




from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Social

@login_required
def listar_social(request):
    social = Social.objects.all()
    return render(request, 'listar_social.html', {'social': social})


@login_required
def eliminar_social(request, social_id):
    social = get_object_or_404(Social, pk=social_id)
    social.delete()
    return redirect('listar_social')



def ver_social(request):
    social_list = Social.objects.all().order_by('-fecha_social')
    paginator = Paginator(social_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        social = paginator.page(page)
    except EmptyPage:
        social = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'social_html': render_to_string('integracion_social.html', {'social': social}),
            'pagination_html': render_to_string('pagination_partial.html', {'social': social}),
        }
        return JsonResponse(data)

    return render(request, 'integracion_social.html', {'social': social})


from django.shortcuts import get_object_or_404
from .models import Social

def detalle_social(request, social_id):
    social = get_object_or_404(Social, pk=social_id)
    return render(request, 'detalle_social.html', {'social': social})




###################################################################################################
#                                    agregar_energetico
###################################################################################################


from django.shortcuts import render, redirect
from .forms import EnergeticoForm, EnergeticoImagen1Form, EnergeticoImagen2Form, EnergeticoImagen3Form, EnergeticoImagen4Form
from .models import Energetico, Energetico_imagen1, Energetico_imagen2, Energetico_imagen3, Energetico_imagen4
from django.contrib.auth.decorators import login_required

@login_required
def admin_agregar_energetico(request):
    energetico_form = EnergeticoForm()
    energetico_imagen_form = EnergeticoImagen1Form()

    context = {'energetico_form': energetico_form, 'energetico_imagen_form': energetico_imagen_form}
    return render(request, 'admin_agregar_energetico.html', context)


@login_required
def publicar_agregar_energetico(request):
    if request.method == 'POST':
        energetico_form = EnergeticoForm(request.POST, request.FILES)
        energetico_imagen_forms = [EnergeticoImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if energetico_form.is_valid() and all(energetico_imagen_form.is_valid() for energetico_imagen_form in energetico_imagen_forms):
            energetico = energetico_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, energetico_imagen_form in enumerate(energetico_imagen_forms, start=1):
                imagen = energetico_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Energetico_imagen{i}'](energetico=energetico, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_energetico')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'energetico_form': energetico_form, 'energetico_imagen_forms': energetico_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_energetico.html', context)

    return admin_agregar_energetico(request)



from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Energetico

@login_required
def listar_energetico(request):
    energetico = Energetico.objects.all()
    return render(request, 'listar_energetico.html', {'energetico': energetico})


@login_required
def eliminar_energetico(request, energetico_id):
    energetico = get_object_or_404(Energetico, pk=energetico_id)
    energetico.delete()
    return redirect('listar_energetico')




def ver_energetico(request):
    energetico_list = Energetico.objects.all().order_by('-fecha_energetico')
    paginator = Paginator(energetico_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        energetico = paginator.page(page)
    except EmptyPage:
        energetico = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'energetico_html': render_to_string('integracion_energetico.html', {'energetico': energetico}),
            'pagination_html': render_to_string('pagination_partial.html', {'energetico': energetico}),
        }
        return JsonResponse(data)

    return render(request, 'eficiencia_energetico.html', {'energetico': energetico})


from django.shortcuts import get_object_or_404
from .models import Energetico

def detalle_energetico(request, energetico_id):
    energetico = get_object_or_404(Energetico, pk=energetico_id)
    return render(request, 'detalle_energetico.html', {'energetico': energetico})


###################################################################################################
#                                    agregar_energetico
###################################################################################################


from django.shortcuts import render, redirect
from .forms import ViviendaForm, ViviendaImagen1Form, ViviendaImagen2Form, ViviendaImagen3Form, ViviendaImagen4Form
from .models import Vivienda, Vivienda_imagen1, Vivienda_imagen2, Vivienda_imagen3, Vivienda_imagen4
from django.contrib.auth.decorators import login_required


@login_required
def admin_agregar_vivienda(request):
    vivienda_form = ViviendaForm()
    vivienda_imagen_form = ViviendaImagen1Form()

    context = {'vivienda_form': vivienda_form, 'vivienda_imagen_form': vivienda_imagen_form}
    return render(request, 'admin_agregar_vivienda.html', context)


@login_required
def publicar_agregar_vivienda(request):
    if request.method == 'POST':
        vivienda_form = ViviendaForm(request.POST, request.FILES)
        vivienda_imagen_forms = [ViviendaImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if vivienda_form.is_valid() and all(vivienda_imagen_form.is_valid() for vivienda_imagen_form in vivienda_imagen_forms):
            vivienda = vivienda_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, vivienda_imagen_form in enumerate(vivienda_imagen_forms, start=1):
                imagen = vivienda_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Vivienda_imagen{i}'](vivienda=vivienda, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_vivienda')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'vivienda_form': vivienda_form, 'vivienda_imagen_forms': vivienda_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_vivienda.html', context)

    return admin_agregar_vivienda(request)



from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Vivienda

@login_required
def listar_vivienda(request):
    vivienda = Vivienda.objects.all()
    return render(request, 'listar_vivienda.html', {'vivienda': vivienda})


@login_required
def eliminar_vivienda(request, vivienda_id):
    vivienda = get_object_or_404(Vivienda, pk=vivienda_id)
    vivienda.delete()
    return redirect('listar_vivienda')



def ver_vivienda(request):
    vivienda_list = Vivienda.objects.all().order_by('-fecha_vivienda')
    paginator = Paginator(vivienda_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        vivienda = paginator.page(page)
    except EmptyPage:
        vivienda = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'vivienda_html': render_to_string('integracion_vivienda.html', {'vivienda': vivienda}),
            'pagination_html': render_to_string('pagination_partial.html', {'vivienda': vivienda}),
        }
        return JsonResponse(data)

    return render(request, 'vivienda_patrimonial.html', {'vivienda': vivienda})


from django.shortcuts import get_object_or_404
from .models import Vivienda

def detalle_vivienda(request, vivienda_id):
    vivienda = get_object_or_404(Vivienda, pk=vivienda_id)
    return render(request, 'detalle_vivienda.html', {'vivienda': vivienda})



###################################################################################################
#                                    agregar_reconstruccion
###################################################################################################


from django.shortcuts import render, redirect
from .forms import ReconstruccionForm, ReconstruccionImagen1Form, ReconstruccionImagen2Form, ReconstruccionImagen3Form, ReconstruccionImagen4Form
from .models import Reconstruccion, Reconstruccion_imagen1, Reconstruccion_imagen2, Reconstruccion_imagen3, Reconstruccion_imagen4
from django.contrib.auth.decorators import login_required

@login_required
def admin_agregar_reconstruccion(request):
    reconstruccion_form = ReconstruccionForm()
    reconstruccion_imagen_form = ReconstruccionImagen1Form()

    context = {'reconstruccion_form': reconstruccion_form, 'reconstruccion_imagen_form': reconstruccion_imagen_form}
    return render(request, 'admin_agregar_reconstruccion.html', context)


@login_required
def publicar_agregar_reconstruccion(request):
    if request.method == 'POST':
        reconstruccion_form = ReconstruccionForm(request.POST, request.FILES)
        reconstruccion_imagen_forms = [ReconstruccionImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if reconstruccion_form.is_valid() and all(reconstruccion_imagen_form.is_valid() for reconstruccion_imagen_form in reconstruccion_imagen_forms):
            reconstruccion = reconstruccion_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, reconstruccion_imagen_form in enumerate(reconstruccion_imagen_forms, start=1):
                imagen = reconstruccion_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Reconstruccion_imagen{i}'](reconstruccion=reconstruccion, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_reconstruccion')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'reconstruccion_form': reconstruccion_form, 'reconstruccion_imagen_forms': reconstruccion_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_reconstruccion.html', context)

    return admin_agregar_reconstruccion(request)



from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Reconstruccion

@login_required
def listar_reconstruccion(request):
    reconstruccion = Reconstruccion.objects.all()
    return render(request, 'listar_reconstruccion.html', {'reconstruccion': reconstruccion})


@login_required
def eliminar_reconstruccion(request, reconstruccion_id):
    reconstruccion = get_object_or_404(Reconstruccion, pk=reconstruccion_id)
    reconstruccion.delete()
    return redirect('listar_reconstruccion')


def ver_reconstruccion(request):
    reconstruccion_list = Reconstruccion.objects.all().order_by('-fecha_reconstruccion')
    paginator = Paginator(reconstruccion_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        reconstruccion = paginator.page(page)
    except EmptyPage:
        reconstruccion = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'reconstruccion_html': render_to_string('integracion_reconstruccion.html', {'reconstruccion': reconstruccion}),
            'pagination_html': render_to_string('pagination_partial.html', {'reconstruccion': reconstruccion}),
        }
        return JsonResponse(data)

    return render(request, 'reconstruccion.html', {'reconstruccion': reconstruccion})


from django.shortcuts import get_object_or_404
from .models import Reconstruccion

def detalle_reconstruccion(request, reconstruccion_id):
    reconstruccion = get_object_or_404(Reconstruccion, pk=reconstruccion_id)
    return render(request, 'detalle_reconstruccion.html', {'reconstruccion': reconstruccion})




###################################################################################################
#                                    agregar_verdes
###################################################################################################

from django.shortcuts import render, redirect
from .forms import VerdesForm, VerdesImagen1Form, VerdesImagen2Form, VerdesImagen3Form, VerdesImagen4Form
from .models import Verdes, Verdes_imagen1, Verdes_imagen2,Verdes_imagen3, Verdes_imagen4
from django.contrib.auth.decorators import login_required

@login_required
def admin_agregar_verdes(request):
    verdes_form = VerdesForm()
    verdes_imagen_form = VerdesImagen1Form()

    context = {'verdes_form': verdes_form, 'verdes_imagen_form': verdes_imagen_form}
    return render(request, 'admin_agregar_verdes.html', context)


@login_required
def publicar_agregar_verdes(request):
    if request.method == 'POST':
        verdes_form = VerdesForm(request.POST, request.FILES)
        verdes_imagen_forms = [VerdesImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if verdes_form.is_valid() and all(verdes_imagen_form.is_valid() for verdes_imagen_form in verdes_imagen_forms):
            verdes = verdes_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, verdes_imagen_form in enumerate(verdes_imagen_forms, start=1):
                imagen = verdes_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Verdes_imagen{i}'](verdes=verdes, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_verdes')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'verdes_form': verdes_form, 'verdes_imagen_forms': verdes_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_verdes.html', context)

    return admin_agregar_verdes(request)


from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Verdes

@login_required
def listar_verdes(request):
    verdes = Verdes.objects.all()
    return render(request, 'listar_verdes.html', {'verdes': verdes})


@login_required
def eliminar_verdes(request, verdes_id):
    verdes = get_object_or_404(Verdes, pk=verdes_id)
    verdes.delete()
    return redirect('listar_verdes')


def ver_verdes(request):
    verdes_list = Verdes.objects.all().order_by('-fecha_verdes')
    paginator = Paginator(verdes_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        verdes = paginator.page(page)
    except EmptyPage:
        verdes = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'verdes_html': render_to_string('integracion_verdes.html', {'verdes': verdes}),
            'pagination_html': render_to_string('pagination_partial.html', {'verdes': verdes}),
        }
        return JsonResponse(data)

    return render(request, 'areas_verdes.html', {'verdes': verdes})


from django.shortcuts import get_object_or_404
from .models import Verdes


def detalle_verdes(request, verdes_id):
    verdes = get_object_or_404(Verdes, pk=verdes_id)
    return render(request, 'detalle_verdes.html', {'verdes': verdes})


###################################################################################################
#                                    agregar_Condominio
###################################################################################################

from django.shortcuts import render, redirect
from .forms import CondominioForm, CondominioImagen1Form, CondominioImagen2Form, CondominioImagen3Form, CondominioImagen4Form
from .models import Condominio, Condominio_imagen1, Condominio_imagen2,Condominio_imagen3, Condominio_imagen4
from django.contrib.auth.decorators import login_required

@login_required
def admin_agregar_condominio(request):
    condominio_form = CondominioForm()
    condominio_imagen_form = CondominioImagen1Form()

    context = {'condominio_form': condominio_form, 'condominio_imagen_form': condominio_imagen_form}
    return render(request, 'admin_agregar_condominio.html', context)

@login_required
def publicar_agregar_condominio(request):
    if request.method == 'POST':
        condominio_form = CondominioForm(request.POST, request.FILES)
        condominio_imagen_forms = [CondominioImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if condominio_form.is_valid() and all(condominio_imagen_form.is_valid() for condominio_imagen_form in condominio_imagen_forms):
            condominio = condominio_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, condominio_imagen_form in enumerate(condominio_imagen_forms, start=1):
                imagen = condominio_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Condominio_imagen{i}'](condominio=condominio, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_condominio')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'condominio_form': condominio_form, 'condominio_imagen_forms': condominio_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_condominio.html', context)

    return admin_agregar_condominio(request)


from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Condominio

@login_required
def listar_condominio(request):
    condominio = Condominio.objects.all()
    return render(request, 'listar_condominio.html', {'condominio': condominio})

@login_required
def eliminar_condominio(request, condominio_id):
    condominio = get_object_or_404(Condominio, pk=condominio_id)
    condominio.delete()
    return redirect('listar_condominio')


def ver_condominio(request):
    condominio_list = Condominio.objects.all().order_by('-fecha_condominio')
    paginator = Paginator(condominio_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        condominio = paginator.page(page)
    except EmptyPage:
        condominio = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'condominio_html': render_to_string('integracion_condominio.html', {'condominio': condominio}),
            'pagination_html': render_to_string('pagination_partial.html', {'condominio': condominio}),
        }
        return JsonResponse(data)

    return render(request, 'condominio_social.html', {'condominio': condominio})


from django.shortcuts import get_object_or_404
from .models import Condominio


def detalle_condominio(request, condominio_id):
    condominio = get_object_or_404(Condominio, pk=condominio_id)
    return render(request, 'detalle_condominio.html', {'condominio': condominio})







###################################################################################################
#                                    agregar_Asbesto
###################################################################################################

from django.shortcuts import render, redirect
from .forms import AsbestoForm, AsbestoImagen1Form, AsbestoImagen2Form, AsbestoImagen3Form, AsbestoImagen4Form
from .models import Asbesto, Asbesto_imagen1, Asbesto_imagen2,Asbesto_imagen3, Asbesto_imagen4
from django.contrib.auth.decorators import login_required

@login_required
def admin_agregar_asbesto(request):
    asbesto_form = AsbestoForm()
    asbesto_imagen_form = AsbestoImagen1Form()

    context = {'asbesto_form': asbesto_form, 'asbesto_imagen_form': asbesto_imagen_form}
    return render(request, 'admin_agregar_asbesto.html', context)

@login_required
def publicar_agregar_asbesto(request):
    if request.method == 'POST':
        asbesto_form = AsbestoForm(request.POST, request.FILES)
        asbesto_imagen_forms = [AsbestoImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if asbesto_form.is_valid() and all(asbesto_imagen_form.is_valid() for asbesto_imagen_form in asbesto_imagen_forms):
            asbesto = asbesto_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, asbesto_imagen_form in enumerate(asbesto_imagen_forms, start=1):
                imagen = asbesto_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Asbesto_imagen{i}'](asbesto=asbesto, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_asbesto')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'asbesto_form': asbesto_form, 'asbesto_imagen_forms': asbesto_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_asbesto.html', context)

    return admin_agregar_asbesto(request)


from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Asbesto

@login_required
def listar_asbesto(request):
    asbesto = Asbesto.objects.all()
    return render(request, 'listar_asbesto.html', {'asbesto': asbesto})

@login_required
def eliminar_asbesto(request, asbesto_id):
    asbesto = get_object_or_404(Asbesto, pk=asbesto_id)
    asbesto.delete()
    return redirect('listar_asbesto')


def ver_asbesto(request):
    asbesto_list = Asbesto.objects.all().order_by('-fecha_asbesto')
    paginator = Paginator(asbesto_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        asbesto = paginator.page(page)
    except EmptyPage:
        asbesto = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'asbesto_html': render_to_string('integracion_asbesto.html', {'asbesto': asbesto}),
            'pagination_html': render_to_string('pagination_partial.html', {'asbesto': asbesto}),
        }
        return JsonResponse(data)

    return render(request, 'asbesto.html', {'asbesto': asbesto})


from django.shortcuts import get_object_or_404
from .models import Asbesto


def detalle_asbesto(request, asbesto_id):
    asbesto = get_object_or_404(Asbesto, pk=asbesto_id)
    return render(request, 'detalle_asbesto.html', {'asbesto': asbesto})

###################################################################################################
#                                    agregar_Asbesto
###################################################################################################


from django.shortcuts import render, redirect
from .forms import ComunitariaForm, ComunitariaImagen1Form, ComunitariaImagen2Form, ComunitariaImagen3Form, ComunitariaImagen4Form
from .models import Comunitaria, Comunitaria_imagen1, Comunitaria_imagen2, Comunitaria_imagen3, Comunitaria_imagen4
from django.contrib.auth.decorators import login_required

@login_required
def admin_agregar_comunitaria(request):
    comunitaria_form = ComunitariaForm()
    comunitaria_imagen_form = ComunitariaImagen1Form()

    context = {'comunitaria_form': comunitaria_form, 'comunitaria_imagen_form': comunitaria_imagen_form}
    return render(request, 'admin_agregar_comunitaria.html', context)

@login_required
def publicar_agregar_comunitaria(request):
    if request.method == 'POST':
        comunitaria_form = ComunitariaForm(request.POST, request.FILES)
        comunitaria_imagen_forms = [ComunitariaImagen1Form(request.POST, request.FILES, prefix=f'imagen{i}') for i in range(1, 5)]

        if comunitaria_form.is_valid() and all(comunitaria_imagen_form.is_valid() for comunitaria_imagen_form in comunitaria_imagen_forms):
            comunitaria = comunitaria_form.save()

            # Guardar las imágenes y asociarlas a la noticia
            for i, comunitaria_imagen_form in enumerate(comunitaria_imagen_forms, start=1):
                imagen = comunitaria_imagen_form.cleaned_data.get('imagen')
                if imagen:
                    nueva_imagen = globals()[f'Comunitaria_imagen{i}'](comunitaria=comunitaria, imagen=imagen)
                    nueva_imagen.save()

            return redirect('admin_agregar_comunitaria')
        else:
            # Manejo de errores o mensajes de validación
            error_message = "Hubo un problema con el formulario. Revise los campos e inténtelo de nuevo."
            context = {'comunitaria_form': comunitaria_form, 'comunitaria_imagen_forms': comunitaria_imagen_forms, 'error_message': error_message}
            return render(request, 'admin_agregar_comunitaria.html', context)

    return admin_agregar_comunitaria(request)


from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Comunitaria

@login_required
def listar_comunitaria(request):
    comunitaria = Comunitaria.objects.all()
    return render(request, 'listar_comunitaria.html', {'comunitaria': comunitaria})

@login_required
def eliminar_comunitaria(request, comunitaria_id):
    comunitaria = get_object_or_404(Comunitaria, pk=comunitaria_id)
    comunitaria.delete()
    return redirect('listar_comunitaria')


def ver_comunitaria(request):
    comunitaria_list = Comunitaria.objects.all().order_by('-fecha_comunitaria')
    paginator = Paginator(comunitaria_list, 18)

    page = request.GET.get('page')

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    try:
        comunitaria = paginator.page(page)
    except EmptyPage:
        comunitaria = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'comunitaria_html': render_to_string('comunitaria.html', {'comunitaria': comunitaria}),
            'pagination_html': render_to_string('pagination_partial.html', {'comunitaria': comunitaria}),
        }
        return JsonResponse(data)

    return render(request, 'comunitaria.html', {'comunitaria': comunitaria})


from django.shortcuts import get_object_or_404
from .models import Comunitaria


def detalle_comunitaria(request, comunitaria_id):
    comunitaria = get_object_or_404(Comunitaria, pk=comunitaria_id)
    return render(request, 'detalle_comunitaria.html', {'comunitaria': comunitaria})



###################################################################################################
#                                    agregar_ubicaciones
###################################################################################################

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UbicacionForm
from .models import Ubicacion
import json

@login_required
def admin_agregar_mapa(request):
    # Lógica para procesar el formulario cuando se envía
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_agregar_mapa')
    else:
        form = UbicacionForm()

    # Obtener ciudades, comunas y lugares para el formulario
    ciudades = Ubicacion.objects.values_list('ciudad', flat=True).distinct()
    comunas = Ubicacion.objects.values_list('comuna', flat=True).distinct()
    lugares = Ubicacion.objects.values_list('nombre_lugar', flat=True).distinct()

    # Obtener ubicaciones y convertirlas a formato JSON
    ubicaciones = Ubicacion.objects.values('nombre_lugar', 'latitud', 'longitud')
    ubicaciones_json = json.dumps(list(ubicaciones), default=str)

    # Obtener la lista de todas las ubicaciones
    ubicaciones_todas = Ubicacion.objects.all()

    context = {
        'form': form,
        'ciudades': ciudades,
        'comunas': comunas,
        'lugares': lugares,
        'ubicaciones_json': ubicaciones_json,
        'ubicaciones': ubicaciones_todas,  # Agrega la lista de ubicaciones
    }

    # Renderizar la plantilla con el contexto
    return render(request, 'admin_agregar_mapa.html', context)

@login_required
def listar_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'listar_ubicaciones.html', {'ubicaciones': ubicaciones})

@login_required
def eliminar_ubicacion(request, ubicacion_id):
    ubicacion = get_object_or_404(Ubicacion, id=ubicacion_id)
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('admin_agregar_mapa')
    return redirect('admin_agregar_mapa')




from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ubicacion
import json

def ver_mapa(request):
    # Obtener todas las ubicaciones
    ubicaciones = Ubicacion.objects.values('nombre_lugar', 'latitud', 'longitud')
    ubicaciones_json = json.dumps(list(ubicaciones), default=str)

    context = {
        'ubicaciones_json': ubicaciones_json,
    }

    return render(request, 'nuestra_mision.html', context)





###################################################################################################
#                                    Iniciar Sesión
###################################################################################################

from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Inicio_Sesion

def iniciar_sesion(request):
    if request.method == 'POST':
        form = Inicio_Sesion(request, request.POST)
        if form.is_valid():
            # Las credenciales son válidas, inicia sesión
            user = form.get_user()
            login(request, user)
            return redirect('perfil')
        else:
            # Las credenciales son inválidas, muestra un mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = Inicio_Sesion()

    return render(request, 'iniciar_sesion.html', {'form': form})
    



###################################################################################################
#                                    Perfil
###################################################################################################

from .models import Usuario

def obtener_datos_de_auth_user():
    usuarios = Usuario.objects.all()

    datos_usuarios = []

    for usuario in usuarios:
        datos_usuario = {
            'username': usuario.username,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'email': usuario.email,
            'cargo': usuario.cargo,
            'telefono': usuario.telefono,
            'fecha_de_nacimiento': usuario.fecha_de_nacimiento,
            'direccion': usuario.direccion,
            'foto_de_perfil': usuario.foto_de_perfil,  # Asegúrate de agregar la imagen de perfil
            'imagen_de_fondo': usuario.imagen_de_fondo,  # Asegúrate de agregar la imagen de fondo
        }
        datos_usuarios.append(datos_usuario)

    return datos_usuarios

    
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from .models import Usuario
from django.contrib import messages

@login_required
def perfil(request):
    try:
        usuario_autenticado = request.user.username
        datos_usuarios = obtener_datos_de_auth_user()
        datos_usuario = next((usuario for usuario in datos_usuarios if usuario['username'] == usuario_autenticado), None)

        context = {
            'usuario': datos_usuario
        }

        return render(request, 'perfil.html', context)
    except Exception as e:
        messages.error(request, f'Error: {e}')
        return redirect('perfil')




@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'perfil.html', {'form': form})


###################################################################################################
#                                 Recuperar contrasenna
###################################################################################################

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import Social, Vivienda, Reconstruccion

def index(request):
    # Obtén las últimas noticias para cada sección
    social = Social.objects.order_by('-fecha_social').first()
    vivienda = Vivienda.objects.order_by('-fecha_vivienda').first()
    reconstruccion = Reconstruccion.objects.order_by('-fecha_reconstruccion').first()

    # Procesa el formulario cuando se envía
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        correo = request.POST.get('correo', '')
        telefono = request.POST.get('telefono', '')
        asunto = request.POST.get('asunto', '')
        mensaje = request.POST.get('mensaje', '')

        try:
            # Validación del formulario (puedes agregar más validaciones según sea necesario)
            if not nombre or not correo or not telefono or not asunto or not mensaje:
                raise ValueError('Todos los campos del formulario son obligatorios.')

            # Crea un objeto EmailMessage
            email = EmailMessage(
                asunto,
                f'Nombre: {nombre}\nCorreo Electrónico: {correo}\nTeléfono: {telefono}\nAsunto: {asunto}\nMensaje: {mensaje}',
                'rukapewma@gmail.com',
                ['rukapewma@gmail.com'],
                reply_to=[correo],
            )

            # Adjunta el archivo (si se proporcionó uno)
            adjunto = request.FILES.get('archivo')
            if adjunto:
                email.attach(adjunto.name, adjunto.read(), adjunto.content_type)

            # Envía el correo
            email.send()

            # Redirige a una página de éxito
            messages.success(request, 'Formulario enviado exitosamente!')

            # Agrega mensajes de depuración
            print(f'Correo enviado a {correo} con asunto: {asunto}')

            return HttpResponseRedirect(reverse('index'))

        except Exception as e:
            # Manejo de errores y muestra un mensaje de error al usuario
            messages.error(request, f'Error al enviar el formulario: {str(e)}')

            # Agrega mensajes de depuración
            print(f'Error al enviar el correo: {str(e)}')

    # Renderiza la plantilla con las últimas noticias y el formulario
    return render(request, 'index.html', {'social': social, 'vivienda': vivienda, 'reconstruccion': reconstruccion})

##############################################################################################


from django.contrib.auth import logout
from django.shortcuts import redirect

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion') 



from django.shortcuts import render

def error_404_view(request, exception=None):
    if request.path.startswith('/admin/'):
        # Redirigir a tu página de error personalizada para solicitudes al admin
        return render(request, 'error_404.html', status=404)
    else:
        # Renderizar la página de error 404 predeterminada para otras solicitudes
        return render(request, 'error_404.html', status=404)