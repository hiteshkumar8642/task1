from django.urls import path
from . import views
urlpatterns = [
path('sign_in/',views.sign_in,name='sign_in'),
path('logout/',views.logout,name='logout'),
path('sign_up/',views.sign_up,name='sign_up'),
path('',views.home, name='home' )
]
