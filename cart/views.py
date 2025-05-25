from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product
from rest_framework.decorators import action


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def add_item(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))
        cart, _ = Cart.objects.get_or_create(user=request.user)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=404)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()
        return Response(CartItemSerializer(item).data, status=201)

    def remove_item(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        try:
            item = CartItem.objects.get(cart=cart, id=pk)
            item.delete()
            return Response(status=204)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found."}, status=404)

class UpdateItems(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["patch"], url_path="update")
    def update_item(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        try:
            item = CartItem.objects.get(cart=cart, id=pk)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found."}, status=404)

        quantity = request.data.get("quantity")
        if not quantity or int(quantity) <= 0:
            return Response({"error": "Quantity must be a positive integer."}, status=400)

        item.quantity = int(quantity)
        item.save()
        return Response(CartItemSerializer(item).data, status=200)
    