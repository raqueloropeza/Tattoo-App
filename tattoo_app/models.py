from django.db import models
from datetime import date, datetime
import re

class Roles(models.Model):
    role = models.CharField(max_length=25)

class Users(models.Model):
    first_name = models.CharField(max_length= 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    birth_date = models.DateField()
    role = models.ForeignKey(Roles, related_name= "user_role", on_delete = models.CASCADE)
        #favorite_artists = list of artists followed by a given user
        #favorite_studios = list of studios followed by a given user
        #studio_comment_by_user = list of studio comments made by a given user
        #profile_comment_by_user= list of users who comment on profile posts
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Locations(models.Model):
    city = models.CharField(max_length = 45)
    state = models.CharField(max_length = 2)

class Styles(models.Model):
    style_name = models.CharField(max_length = 45)
    style_desc = models.TextField(null=True)
        #artists_with_styles = list of styles linked to a given artist
        #studio_with_styles = list of styles linked to a given studio

class Profile(models.Model):
    username = models.CharField(max_length = 45)
    user = models.ForeignKey(Users, related_name="user", on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/', null=True)
    website = models.CharField(max_length = 200, null = True)
    bio = models.TextField(null= True)
    location = models.ForeignKey(Locations, related_name ="user_location", on_delete = models.CASCADE)
    books_open = models.BooleanField()
    walk_ins = models.BooleanField()
    is_apprentice = models.BooleanField()
    styles = models.ManyToManyField(Styles, related_name= "artists_with_styles")
    followers = models.ManyToManyField(Users, related_name = "favorite_artists")
        #users who follow artist profile
        #studios_joined = list of studios an artist has worked at. 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class ProfilePosts(models.Model):
    profile = models.ForeignKey(Profile, related_name = "profile_post", on_delete = models.CASCADE)
    image = models.ImageField(upload_to= 'images/')
    description = models.TextField (null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class ProfileComments (models.Model):
    comment = models.ForeignKey(ProfilePosts, related_name = "profile_comments", on_delete = models.CASCADE)
    user_comment = models.ManyToManyField(Users, related_name = "profile_comment_by_user")
        #users who comment on profile posts


class Studios(models.Model):
    studio_name = models.CharField(max_length = 255)
    location = models.ForeignKey(Locations, related_name = "studio_location", on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/', null=True)
    website = models.CharField(max_length = 200, null = True)
    bio = models.TextField(null = True)
    walk_ins = models.BooleanField()
    styles = models.ManyToManyField(Styles, related_name = "studio_with_styles")
    artists_at_studio = models.ManyToManyField(Profile, related_name = "studios_joined")
    followers = models.ManyToManyField(Users, related_name = "favorite_studios")
        #users who follow studios
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class StudioPosts(models.Model):
    studio = models.ForeignKey(Studios, related_name = "studio_post", on_delete = models.CASCADE)
    image = models.ImageField(upload_to= 'images/')
    description = models.TextField (null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class StudioComments (models.Model):
    comment = models.ForeignKey(StudioPosts, related_name = "studio_comments", on_delete = models.CASCADE)
    user_comment = models.ManyToManyField(Users, related_name = "studio_comment_by_user")
        #users who comment on studio posts