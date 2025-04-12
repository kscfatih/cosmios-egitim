from rest_framework.views import APIView
from web_site.models import Category, Product, Contact, Reservation
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,MyPermission


@api_view(['GET','POST'])
@permission_classes([MyPermission])
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
        
class CategoryGenericViewListCreate(generics.ListCreateAPIView):
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        print(self.request.user)
        return Category.objects.filter(status=True)

class CategoryGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.filter(status=True)
    serializer_class = CategoryModelSerializer

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategoryModelSerializer

class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategoryModelSerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.filter(status=True)
    serializer_class = ProductSerializer


class ContactApiView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self, request, id=None):
        if id:
            contact = Contact.objects.get(id=id)
            serializer = ContactSerializer(contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            contacts = Contact.objects.filter(status=True)
            serializers = ContactSerializer(contacts, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, id=None):
        if id:
            contact = Contact.objects.get(id=id)
        else:
            contact = Contact.objects.get(id=request.data['id'])
        
        serializer = ContactSerializer(contact, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, id):
        contact = Contact.objects.get(id=id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReservationViewset(ModelViewSet):
    queryset = Reservation.objects.filter(status=True)
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
