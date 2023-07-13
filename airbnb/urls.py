from django.urls import include, path

urlpatterns = [
    path('User/', include('User.urls')),
]
