from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Settings(BaseModel):
    address = models.TextField(verbose_name='Adres')
    phone = models.CharField(max_length=11, verbose_name='Telefon', unique=True)
    email = models.EmailField(unique=True, verbose_name='Email')
    opening_time = models.CharField(max_length=50, verbose_name='Çalışma saatleri')
    welcome_message = models.CharField(max_length=75, verbose_name='Hoşgeldiniz mesajı')
    home_header_text = models.TextField(verbose_name='Ana sayfa header yazı')
    home_header_big_text_1 = models.CharField(max_length=50, verbose_name='Ana sayfa header büyük yazı sol')
    home_header_big_text = models.TextField(verbose_name='Ana sayfa header büyük yazı sağ')
    home_header_button = models.CharField(max_length=50, verbose_name='Ana sayfa Header button')
    home_header_button_link = models.URLField(verbose_name='Ana sayfa Header button URL', null=True, blank=True)
    footer_text = models.CharField(max_length=150, verbose_name='Footer yazı')
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return 'Site Ayar'

class SubText(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sub-text/')
    content = models.TextField()
    button_title = models.CharField(max_length=30)
    button_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class Contact(BaseModel):
    name = models.CharField(max_length=30, verbose_name='İsim')
    email = models.EmailField(verbose_name='E-posta')
    phone = models.CharField(max_length=11, verbose_name='Telefon')
    message = models.TextField(verbose_name='Mesajınız')

    def __str__(self):
        return self.name
    

class Reservation(BaseModel):
    name = models.CharField(max_length=30, verbose_name='İsim')
    email = models.EmailField(verbose_name='E-posta')
    phone = models.CharField(max_length=11, verbose_name='Telefon')
    message = models.TextField(verbose_name='Mesajınız')
    datetime = models.DateTimeField()
    how_many_guests = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    

class Product(BaseModel):
    name = models.CharField(max_length=50)
    m_price = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Orta Boy')
    l_price = models.DecimalField(decimal_places=2,max_digits= 5,  verbose_name='Büyük Boy')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name

