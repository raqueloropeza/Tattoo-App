from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import re
from datetime import date, datetime
from time import strftime, strptime

def main(request):
    context = {
        "all_profiles": Profile.objects.all(),
        "all_studios": Studios.objects.all(),
    }
    return render(request, "main.html", context)

def register(request):
    context = {
        "all_roles": Roles.objects.all(),
    }
    return render(request,"register.html", context)

def createUser(request):
    role = Roles.objects.get(id= int(request.POST['role']))
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    this_user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email= request.POST['email'], password= pw_hash, birth_date = request.POST['birth_date'], role = role)
    request.session['user_id'] = this_user.id
    print(this_user.id)
    return redirect('/register/profile')

def newProfile(request):
    context = {
        "this_user": Users.objects.get(id=request.session['user_id']),
        "all_locations": Locations.objects.all(),
    }

    return render(request, "profileform.html", context)

def createProfile(request):
    user = Users.objects.get(id=request.session['user_id'])
    location = Locations.objects.get(id= int(request.POST['location']))
    books_open = False
    if(request.POST['books'] == "open"):
        books_open = True 
    walk_ins = False
    if(request.POST['walkins'] == "yes"):
        walk_ins = True
    is_apprentice = False
    if(request.POST['apprentice'] == "yes"):
        is_apprentice = True

    this_profile = Profile.objects.create(username = request.POST['username'], user =  user, bio = request.POST['bio'], location = location, books_open= books_open, walk_ins = walk_ins, is_apprentice = is_apprentice)
    request.session['profile_id'] = this_profile.id
    return redirect("/")

def ProfilePage(request):
    user = Users.objects.get(id= request.session['user_id'])
    profile = Profile.objects.get(id= request.session['profile_id'])
    context= {
        "profile_styles": Profile.objects.get(id= profile.id).styles.all(),
        "all_styles": Styles.objects.all(),
        "profile_studios": Profile.objects.get(id= profile.id).studios_joined.all(),
        "all_studios": Studios.objects.all(),
        "this_profile": Profile.objects.get(id= profile.id),
    }
    return render(request, "profile.html", context)



        
