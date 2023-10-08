from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.registration, name="registration"),
    path('login/',views.login_request, name="login"),
    path('logout/', views.logout_request, name='logout'),
    path('earth/', views.earth, name='Earth'),
    path('mars/', views.mars, name='mars'),
    path('moon/', views.moon, name='moon'),
    path('ship/', views.ship, name='ship'),
    path('station/', views.station, name='station'),
]
