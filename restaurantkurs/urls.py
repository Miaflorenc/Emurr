from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('api/v2/', include('feedbacks.urls')),
    path('api/v4/', include('booking.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
