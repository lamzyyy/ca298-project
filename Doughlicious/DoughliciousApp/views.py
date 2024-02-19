from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import * 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from .validators import *


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/previousOrders/')


class UserLoginView(LoginView):
    template_name='login.html'

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required
def previousOrders(request):
    orders = order.objects.filter(user=request.user)
    return render(request, 'previousOrders.html', {'orders':orders})

def base(request):
    return render(request, 'base.html') 

@login_required
def createPizza(request):
    if request.method == "POST":
        form = createPizzaForm(request.POST)
        if form.is_valid():
            #this creates a pizza instance from the form 
            pizza = form.save()
            return redirect('/deliveryDetails/' + str(pizza.pizzaId) + '/')
    else:
        form = createPizzaForm()
    return render(request, 'createPizza.html', {'form': form})

@login_required
def specificOrder(request, orderId):
    order_instance = get_object_or_404(order, id=orderId)
    return render(request, 'specificItem.html', {'order' : order_instance})

@login_required
def createDeliveryDetails(request, pizzaId):
    pizza = get_object_or_404(Pizza, pizzaId=pizzaId)

    if request.method == "POST":
        form = createDeliveryDetailsForm(request.POST)
        try:
            if form.is_valid():
                delivery_details = form.save()
                order_instance = order.objects.create(user=request.user, deliveryDetails=delivery_details, pizza=pizza)
            return redirect("/messege/" + str(order_instance.id) + "/")
        
        except ValueError as e:
            error_message = str(e)
            form.add_error('cardNum', error_message)
            return render(request, 'createDeliveryDetails.html', {'form': form})
    else:
        form = createDeliveryDetailsForm()
        return render(request, 'createDeliveryDetails.html', {'form': form})

'''
def createDeliveryDetails(request, pizzaId):
    if request.method == "POST":
        form = createDeliveryDetailsForm(request.POST)
        if form.is_valid():
            deliveryDetails = form.save()
            pizza = get_object_or_404(Pizza, pizzaId=pizzaId)
            Order = order.objects.create(user=request.user, deliveryDetails=deliveryDetails)
            Order.pizza.set([pizza])
            return redirect("/messege/" + str(Order.id) + "/")
        
        else:
            try:
                form.cleaned_data['cardNum'] = validate_cardNum(form.cleaned_data['card'])
            except ValueError as e:
                error_message = str(e)
                form.add_error('card_number', error_message)
    else:
        form = createDeliveryDetailsForm()
    return render(request, 'createDeliveryDetails.html', {'form': form})'''

@login_required
def showMessege(request, orderId):
    messege = 'Thank you for ordering!'
    instance = get_object_or_404(order, id=orderId)
    return render(request, 'messege.html', {'Messege': messege, 'order': instance})