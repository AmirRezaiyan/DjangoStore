from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart, CartItem

class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response({"error": "Cart is empty."}, status=400)

        order = Order.objects.create(user=request.user)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # پاک‌سازی سبد خرید بعد از ثبت سفارش
        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)
