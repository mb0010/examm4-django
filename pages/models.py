from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=200)
    janr = models.CharField(max_length=100)  
    date = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/images')
    film = models.FileField(upload_to='static/videos')  
    treiler = models.FileField(upload_to='static/videos') 

    def __str__(self):
        return self.name

class Ticket(models.Model):
    place = models.CharField(max_length=50)  
    vip = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.place} - {'VIP' if self.vip else 'Regular'}"

class Theatr(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class OnlineShop(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    place = models.CharField(max_length=50) 
    quantity = models.PositiveIntegerField()  
    phone_number = models.CharField(max_length=15)  
    theatr = models.ForeignKey(Theatr, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} tickets for {self.film.name} at {self.theatr.name}"

class User(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=15, unique=True)  
    email = models.EmailField(max_length=255, unique=True)  
    username = models.CharField(max_length=150, unique=True)  

    def __str__(self):
        return f"{self.username} ({self.name} {self.last_name})"

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    online_shop = models.ForeignKey(OnlineShop, on_delete=models.CASCADE)  
    order_date = models.DateTimeField(auto_now_add=True)  
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  
    status = models.CharField(max_length=50, choices=[
        ('online', 'cash')
    ], default='pending') 
    def __str__(self):
        return f"Order by {self.user.username} - {self.status}"
