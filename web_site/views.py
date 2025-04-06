from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Settings, Category, Contact as ContactModel, Reservation as ReservationModel
from django.contrib import messages
import datetime



def settings_context(request):
    return {'settings':Settings.objects.first()}

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class Reservation(View):
    def get(self, request):
        return render(request, 'reservation.html')
    
    def post(self, request):
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        datetime_ = date +' '+ time # 2025-04-12 16:00
        cozumlenmis = datetime.datetime.strptime(datetime_, '%Y-%m-%d %H:%M')

        if ReservationModel.objects.filter(datetime=cozumlenmis).exists():
            messages.error(request, 'Daha önce bu zamanda rezervasyon yapılmış')
            return redirect('reservation')

        ReservationModel.objects.create(
            name = name,
            email = email,
            phone = phone,
            message = message,
            datetime = cozumlenmis,
            how_many_guests = int(guests)
        )
        messages.success(request, 'Rezervasyon başarılı şekilde yapılmıştır')
        return redirect('reservation')
    


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        ContactModel.objects.create(name=name, email=email,phone=phone,message=message)
        messages.success(request, 'Mesajınız alındı ! En kısa sürede iletişime geçilecek !')
        return redirect('contact')

class Menu(View):
    def get(self, request):
        categories = Category.objects.filter(status=True)
        return render(request, 'menu.html', {'categories':categories})