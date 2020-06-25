from django.contrib import admin
from django.urls import path
from Contact import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.Contacts),
    path('delete_contact/<int:contact_id>/',views.delete_contact),
    path('edit_contact/<int:contact_id>/',views.edit_contact),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)