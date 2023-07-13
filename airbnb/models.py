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
    rating = models.FloatField()

    def __str__(self):
        return self.username
    
    def is_super_host(self):
        return self.is_superhost
    
class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role

class Properties(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=50)
    lat_long = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    photo = models.CharField(max_length=255)
    guests_allowed = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    beds = models.IntegerField()