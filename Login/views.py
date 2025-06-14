from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EmailRegistrationForm
from django.shortcuts import render, redirect
from .forms import PaymentForm
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit
from decimal import Decimal




def login_user(request):
    # Example login logic
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_index')  # Adjust to your homepage route
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'Login/login.html')  # Make sure this template exists

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = EmailRegistrationForm()
    
    return render(request, 'Login/register_user.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # or 'email' if you're using email to log in
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # You can also check is_superuser
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'Login/adminLogin.html')


def admin_logout(request):
    logout(request)
    return redirect('adminLogin')

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Convert Decimal values to float
            for key, value in data.items():
                if isinstance(value, Decimal):
                    data[key] = float(value)

            request.session['payment_data'] = data
            return redirect('receipt')
    else:
        form = PaymentForm()
    return render(request, 'Login/payment.html', {'form': form})

def receipt_view(request):
    data = request.session.get('payment_data')
    if not data:
        return redirect('payment')
    return render(request, 'Login/receipt.html', {'data': data})

def receipt_pdf_view(request):
    data = request.session.get('payment_data')
    if not data:
        return redirect('payment')
    
    template = get_template('Login/receipt.html')
    html = template.render({'data': data})
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="receipt.pdf"'
    return response