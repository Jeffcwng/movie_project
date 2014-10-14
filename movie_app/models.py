from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Watcher(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format: 415-111-2222")
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.username)

class Theater(models.Model):
    cinema_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=20, blank=True)
    # zipcodes are better off as charfields, they can start with a 0 which makes them not integers
    zip_code = models.IntegerField(max_length=5, blank=True)

    def __unicode__(self):
        return u"{}".format(self.cinema_name)

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    minutes = models.IntegerField()
    genre = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    main_cast = models.CharField(max_length=30)
    cinema = models.ForeignKey(Theater, related_name='movies')

    def __unicode__(self):
        return u"{}".format(self.movie_name)

class Showtime(models.Model):
    section = models.CharField(max_length=50)
    show_section = models.ForeignKey(Movie, related_name='show_times')

    def __unicode__(self):
            return u"{}".format(self.section)

class Seat(models.Model):
    seat_num = models.CharField(max_length=3)
    show_num = models.ForeignKey(Showtime, related_name='seat_numbers')
    user = models.ForeignKey(Watcher, null=True, related_name='seats')

    class Meta:
        ordering = ['seat_num']

    def __unicode__(self):
            return u"{}".format(self.seat_num)

class Ticket(models.Model):
    seat_ticket = models.ForeignKey(Watcher, null=True, related_name='user_tickets')
    # shouldn't a ticket be for a specific seat, not a movie?
    for_movie = models.ForeignKey(Movie, null=True, related_name='seats')
    paid = models.BooleanField(default=False)
