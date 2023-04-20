from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        field = (
            "price",
            "product",
            "quanity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItem(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.Objects.create(order=order, **item_data)


    

    d
