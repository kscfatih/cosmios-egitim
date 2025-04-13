from rest_framework import serializers
from web_site.models import Category, Product, Contact, Reservation



class ProductSerializer_(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    m_price = serializers.DecimalField(decimal_places=2, max_digits=5)
    l_price = serializers.DecimalField(decimal_places=2,max_digits= 5)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    status = serializers.BooleanField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.m_price = validated_data.get('m_price', instance.m_price)
        instance.l_price = validated_data.get('l_price', instance.l_price)
        instance.category = validated_data.get('category', instance.category)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    status = serializers.BooleanField()
    name = serializers.CharField(max_length=50)
  
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Product
        fields = '__all__'

class CategoryModelSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=11)
    message = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    status = serializers.BooleanField(default=True)

    def validate_message(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Mesajınız 10 karakterden küçük olmamalıdır')

    def validate_phone(self, value):
        if value[0] != '0':
            raise serializers.ValidationError('Telefon numarası 0 ile başlamalı')


    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.message = validated_data.get('message', instance.message)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'