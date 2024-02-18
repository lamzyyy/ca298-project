from django.urls import path
from . import views
from .forms import *

urlpatterns = [
   path('', views.UserSignupView.as_view(), name="register"),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
   path('logout/', views.logout_user, name="logout"),
   path('Pizza/', views.createPizza, name="createPizza"),
   path('previousOrders/', views.previousOrders, name="previousOrders"),
   path('deliveryDetails/<int:pizzaId>/', views.createDeliveryDetails, name="deliveryDetails"),
   path('messege/<int:orderId>/', views.showMessege, name="messege"),
   path('orders/<int:orderId>', views.specificOrder, name="specificOrder"),
]