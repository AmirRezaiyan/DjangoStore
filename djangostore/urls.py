from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),   
    path('api/cart/', include('cart.urls')), 
    path('api/', include('orders.urls')),
]
