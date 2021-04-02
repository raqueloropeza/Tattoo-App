from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import *
import bcrypt
import re
from datetime import date, datetime
from time import strftime, strptime

def main(request):
    context = {
        "all_users":Users.objects.all(),
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
    errors = Users.objects.basic_validator(request.POST)
    if errors: 
        for key, value in errors.items():
                messages.error(request, value)
        return JsonResponse({key:val})
    else: 
        role = Roles.objects.get(id= int(request.POST['role']))
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        this_user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email= request.POST['email'], password= pw_hash, birth_date = request.POST['birth_date'], role = role)
        request.session['user_id'] = this_user.id
        print(this_user.id)
        return JsonResponse({"message": "Request Success!"})

def newProfile(request):
    mapbox_access_token =  "pk.eyJ1Ijoicm9ja3V6YWtpIiwiYSI6ImNrbXdvanBlMzBoMGMybnA1MDQ1MXRxd2EifQ.QYEOIs2oTEInYtbs1u-wBw"
    context = {
        "this_user": Users.objects.get(id=request.session['user_id']),
        "all_locations": Locations.objects.all(),
    }

    return render(request, "profileform.html", context, {'mapbox_access_token':mapbox_access_token})

def createProfile(request):
    user = Users.objects.get(id=request.session['user_id'])
    location = Locations.objects.get(id= int(request.POST['location']))
    
    walk_ins = False
    if(request.POST['walkins'] == "yes"):
        walk_ins = True
    is_apprentice = False
    if(request.POST['apprentice'] == "yes"):
        is_apprentice = True

    this_profile = Profile.objects.create(user =  user, bio = request.POST['bio'], deposit = request.POST['deposit'], location = location, availability= request.POST['availability'], walk_ins = walk_ins, is_apprentice = is_apprentice)
    request.session['profile_id'] = this_profile.id
    return JsonResponse({"message": "Request Success!"})

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

class AddProfileView(CreateView):
    model = Profile
    template_name = "createprofile.html"
    success_url = "/"
    fields = ("user","availability", "walk_ins","is_apprentice","deposit","location", "address" ) 



        
