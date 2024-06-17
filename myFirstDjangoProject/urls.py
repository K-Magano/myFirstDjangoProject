
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # telling Django to include our urls aka mapping
    path('',include('plp_Ecommerce.urls')),
    
]

