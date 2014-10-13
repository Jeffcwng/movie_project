from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from movie_app.models import *

admin.site.register(Watcher)

admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Seat)


