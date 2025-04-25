from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from xiaomijiaju.views import product_list, custom_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),
    path('xiaomijiaju/', include('xiaomijiaju.urls')),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
     path('logout/', custom_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)