from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("catalog.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include('accounts.urls')),
    path('cart/', include("cart.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

