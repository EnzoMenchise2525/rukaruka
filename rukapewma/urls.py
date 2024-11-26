"""rukapewma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', views.error_404_view, name="admin-error-404"),
    path('error_404/', views.error_404, name="error_404"),
    
    path('', views.index, name="index"),
    
    path('nuestra_mision/', views.ver_mapa, name="nuestra_mision"),
    
    # Vistas de los Administradores
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('login/', views.iniciar_sesion, name='login'),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
   
    
    # Otras URLs de los administradores
    path('integracion_social/', views.ver_social, name="integracion_social"),
    path('admin_agregar_intSocial/', views.admin_agregar_intSocial, name="admin_agregar_intSocial"),
    path('publicar_agregar_intSocial/', views.publicar_agregar_intSocial, name='publicar_agregar_intSocial'),
    
    path('listar_social/', views.listar_social, name='listar_social'),
    path('eliminar_social/<int:social_id>/', views.eliminar_social, name='eliminar_social'),
    path('detalle_social/<int:social_id>/', views.detalle_social, name='detalle_social'),
    
    # Otras URLs de los administradores
    path('eficiencia_energetico/', views.ver_energetico, name="eficiencia_energetico"),
    path('admin_agregar_energetico/', views.admin_agregar_energetico, name="admin_agregar_energetico"),
    path('publicar_agregar_energetico/', views.publicar_agregar_energetico, name="publicar_agregar_energetico"),
    
    path('listar_energetico/', views.listar_energetico, name='listar_energetico'),
    path('eliminar_energetico/<int:energetico_id>/', views.eliminar_energetico, name='eliminar_energetico'),
    path('detalle_energetico/<int:energetico_id>/', views.detalle_energetico, name='detalle_energetico'),
    
        # Otras URLs de los administradores
    path('vivienda_patrimonial/', views.ver_vivienda, name="vivienda_patrimonial"),
    path('admin_agregar_vivienda/', views.admin_agregar_vivienda, name="admin_agregar_vivienda"),
    path('publicar_agregar_vivienda/', views.publicar_agregar_vivienda, name="publicar_agregar_vivienda"),
    
    path('listar_vivienda/', views.listar_vivienda, name='listar_vivienda'),
    path('eliminar_vivienda/<int:vivienda_id>/', views.eliminar_vivienda, name='eliminar_vivienda'),
    path('detalle_vivienda/<int:vivienda_id>/', views.detalle_vivienda, name='detalle_vivienda'),
    
    
        # Otras URLs de los administradores
    path('reconstruccion/', views.ver_reconstruccion, name="reconstruccion"),
    path('admin_agregar_reconstruccion/', views.admin_agregar_reconstruccion, name="admin_agregar_reconstruccion"),
    path('publicar_agregar_reconstruccion/', views.publicar_agregar_reconstruccion, name="publicar_agregar_reconstruccion"),
    
    path('listar_reconstruccion/', views.listar_reconstruccion, name='listar_reconstruccion'),
    path('eliminar_reconstruccion/<int:reconstruccion_id>/', views.eliminar_reconstruccion, name='eliminar_reconstruccion'),
    path('detalle_reconstruccion/<int:reconstruccion_id>/', views.detalle_reconstruccion, name='detalle_reconstruccion'),
    
    
        # Otras URLs de los administradores
    path('areas_verdes/', views.ver_verdes, name="areas_verdes"),
    path('admin_agregar_verdes/', views.admin_agregar_verdes, name="admin_agregar_verdes"),
    path('publicar_agregar_verdes/', views.publicar_agregar_verdes, name="publicar_agregar_verdes"),
    
    path('listar_verdes/', views.listar_verdes, name='listar_verdes'),
    path('eliminar_verdes/<int:verdes_id>/', views.eliminar_verdes, name='eliminar_verdes'),
    path('detalle_verdes/<int:verdes_id>/', views.detalle_verdes, name='detalle_verdes'),
    
    
    # Otras URLs de los administradores
    path('condominio_social/', views.ver_condominio, name="condominio_social"),
    path('admin_agregar_condominio/', views.admin_agregar_condominio, name="admin_agregar_condominio"),
    path('publicar_agregar_condominio/', views.publicar_agregar_condominio, name="publicar_agregar_condominio"),
    
    path('listar_condominio/', views.listar_condominio, name='listar_condominio'),
    path('eliminar_condominio/<int:condominio_id>/', views.eliminar_condominio, name='eliminar_condominio'),
    path('detalle_condominio/<int:condominio_id>/', views.detalle_condominio, name='detalle_condominio'),
    
    
    # Otras URLs de los administradores
    path('asbesto/', views.ver_asbesto, name="asbesto"),
    path('admin_agregar_asbesto/', views.admin_agregar_asbesto, name="admin_agregar_asbesto"),
    path('publicar_agregar_asbesto/', views.publicar_agregar_asbesto, name="publicar_agregar_asbesto"),
    
    path('listar_asbesto/', views.listar_asbesto, name='listar_asbesto'),
    path('eliminar_asbesto/<int:asbesto_id>/', views.eliminar_asbesto, name='eliminar_asbesto'),
    path('detalle_asbesto/<int:asbesto_id>/', views.detalle_asbesto, name='detalle_asbesto'),
    

    # Otras URLs de los administradores
    path('comunitaria/', views.ver_comunitaria, name="comunitaria"),
    path('admin_agregar_comunitaria/', views.admin_agregar_comunitaria, name="admin_agregar_comunitaria"),
    path('publicar_agregar_comunitaria/', views.publicar_agregar_comunitaria, name="publicar_agregar_comunitaria"),
    
    path('listar_comunitaria/', views.listar_comunitaria, name='listar_comunitaria'),
    path('eliminar_comunitaria/<int:comunitaria_id>/', views.eliminar_comunitaria, name='eliminar_comunitaria'),
    path('detalle_comunitaria/<int:comunitaria_id>/', views.detalle_comunitaria, name='detalle_comunitaria'),
    
   
    # agregar ubicacion
    path('listar_ubicaciones/', views.listar_ubicaciones, name='listar_ubicaciones'),
    path('eliminar_ubicacion/<int:ubicacion_id>/', views.eliminar_ubicacion, name='eliminar_ubicacion'),
    path('admin_agregar_mapa/', views.admin_agregar_mapa, name='admin_agregar_mapa'),
   
    # Recuperar contrasenna
   
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

       