from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'is_paid', 'items', 'total_items']

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())