from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    profile_picture = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def is_super_host(self):
        return self.is_superhost