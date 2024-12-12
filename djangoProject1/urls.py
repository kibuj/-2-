from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.home, name='home'),
    path('homeA/', views.homeA, name='homeA'),
    path('homeB/', views.homeB, name='homeB'),
    path('homeC/', views.homeC, name='homeC'),
    path('homeD/', views.homeD, name='homeD'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
