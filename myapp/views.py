from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Product, OrderProduct


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = request.POST.get('email')

            user = form.save(commit=False)
            user.email = email
            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'sign/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'sign/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homes/home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')  # profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'sign/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'sign/login.html', {'form': form})


def home(request):
    return render(request, 'homes/home.html')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)

    order_product, product_created = OrderProduct.objects.get_or_create(order=order, product=product)

    if product_created:
        order_product.quantity = 1
    else:
        order_product.quantity += 1

    order_product.save()
    return redirect('/cart')

#Крінж і халтура, хз чого не зробив шаблонізатором
def homeA(request):
    return render(request, 'homes/homeA.html')


def homeB(request):
    return render(request, 'homes/homeB.html')


def homeC(request):
    return render(request, 'homes/homeC.html')


def homeD(request):
    return render(request, 'homes/homeD.html')


def view_cart(request):
    order = Order.objects.filter(user=request.user, is_ordered=False).first()
    if order:
        order_products = OrderProduct.objects.filter(order=order)
    else:
        order_products = []

    return render(request, 'cart.html', {'order_products': order_products})



def profile(request):
    return render(request, 'profile.html')


def signout(request):
    logout(request)
    return redirect('/')


