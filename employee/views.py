from django.shortcuts import render

def home(request):
    return render(request, "home.html")       

def user_login(request):
    return render(request,"user_login.html")

def admin_login(request):
    return render(request,"admin_login.html")

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def signup_login(request):
    return render(request,"signup_login.html")

def user_dashboard(request):
    return render(request, "user_dashboard.html")
