from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.views.static import serve
from django.conf.urls import url

admin.site.site_header = "Image Uploader Admin Portal"
admin.site.site_title = "Image Uploader Admin Portal"
admin.site.index_title = "Wellcome, Image Uploader"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("login", views.loginUser),
    path("logout", views.logoutUser),
    path("deleteimg", views.deleteimg),
    path("delete/<int:id>", views.delete, name='delete'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler404 = 'myapp.views.error_404_view'
# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
