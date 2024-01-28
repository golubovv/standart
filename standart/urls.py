from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payment.urls')),
    path('ajax/', include('ajax.urls')),
    path('users/', include('user.urls'))
]
