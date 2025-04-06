from rest_framework.views import APIView
from web_site.models import Category, Product
from rest_framework.response import Response
from .serializer import CategorySerializer, ProductSerializer, ProductSerializer_
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def products_api_view(request):
    if request.method == 'POST':
        serializer = ProductSerializer_(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        products = Product.objects.filter(status=True)
        serializer = ProductSerializer_(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.filter(status=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryApiView(APIView):
    def get(self, request, id=None):
        if id:
            category = self.get_category(id)
            
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            categories = Category.objects.filter(status=True)
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, id):
        category = self.get_category(id)
        
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        category = self.get_category(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    @staticmethod
    def get_category(id):
        try:
            category = Category.objects.get(id=id)
            return category
        except:
            return Response('Belirtilen id\'de bir kayıt bulunamadı ! ', status=status.HTTP_204_NO_CONTENT)