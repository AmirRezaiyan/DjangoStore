from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, UpdateItems

router = DefaultRouter()
router.register(r'items', UpdateItems, basename='cart')

cart_view = CartViewSet.as_view({
    'get': 'list',
    'post': 'add_item',
})

urlpatterns = [
    path('cart/', cart_view, name='cart-detail'),
    path('cart/remove/<int:pk>/', CartViewSet.as_view({'delete': 'remove_item'}), name='cart-remove'),
    path('', include(router.urls)),  # این خط بسیار مهمه!
]
