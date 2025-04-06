from rest_framework import serializers
from web_site.models import Category, Product



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
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'