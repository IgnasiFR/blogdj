"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
