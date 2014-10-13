from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from movie_app.models import *
from movie_project import settings
from movie_app.forms import *
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib.auth import login, authenticate
import braintree
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                      merchant_id="b2t64c23842v23fk",
                                      public_key="dbrbtktrfttfyryp",
                                      private_key="135f6a800d9f04bbd92acac101066bef")

# Create your views here.

def home(request):
    return render(request, "home.html")

@csrf_exempt
def about(request):
    return render(request, "about.html")

@login_required
@csrf_exempt
def buyticket(request):
    return render(request, "buyticket.html")

@csrf_exempt
def contact(request):
    return render(request, "contact.html")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            # <h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>
            html_content = '<div style="width:500px;">' \
                           '<table width="100%" border="0" align="center" cellpadding="5" style="background: #ffffff; border-right: 1px solid #cccccc; border-left: 1px solid #cccccc; border-top: 1px solid #cccccc; border-bottom: 1px solid #cccccc;">' \
                           '<tr><td valign="bottom"><table width="100%" height="75px;" border="0" style=" background-color:#285e8e; padding-left:10px;">' \
                           '<tr><td align="left" valign="bottom"><span style="color:#fff; padding-bottom:5px; font-size:22px; font-family:Arial, Helvetica, sans-serif; letter-spacing:2px;"><strong>Movie Booking</strong></span></td></tr></table></td></tr>' \
                           '<tr><td><div style="padding:5px; color:#555555; font-family: Arial, Helvetica, sans-serif;"><h2>Hi {}, thank you for signing up!</h2> I hope you enjoy using our site!</div></td></tr>' \
                           '<tr><td><table width="100%" height="20px;" border="0" style=" background-color:#285e8e;"><tr><td align="left" valign="bottom">&nbsp;</td></tr></table></td></tr></table></div>'.format(user.username)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("/profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@csrf_exempt
@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("registration/login")
    return render(request, "registration/profile.html")

@csrf_exempt
def movie_ajax(request):
    return render(request, "movie/movie.html")

@csrf_exempt
def showtime_ajax(request):
    return render(request, "showtime/showtime.html")

@csrf_exempt
def movie(request):
    # movie = Movie.objects.all()
    # print movie
    # data = serializers.serialize('json', movie)
    # print data
    # return HttpResponse(data, content_type='application/json')
    movies = Movie.objects.all()
    return render(request, "movie/movie2.html", {'movies': movies})

@csrf_exempt
def view_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    data = {'movie': movie}
    return render(request, "movie/view_movie2.html", data)

@csrf_exempt
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/movie")
    else:
        form = MovieForm()
    data = {'form': form}
    return render(request, "movie/add_movie2.html", data)

@csrf_exempt
def showtime(request):
    showtimes = Showtime.objects.all()
    return render(request, "showtime/showtime2.html", {'showtimes':showtimes})

@csrf_exempt
def view_showtime(request, showtime_id):
    showtime = Showtime.objects.get(id=showtime_id)
    data = {'showtime': showtime}
    return render(request, "showtime/view_showtime2.html", data)

@csrf_exempt
def add_showtime(request):
    if request.method == "POST":
        form = ShowtimeForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/showtime")
    else:
        form = ShowtimeForm()
    data = {'form': form}
    return render(request, "showtime/add_showtime2.html", data)

@login_required
@csrf_exempt
def seat(request):
    seats = Seat.objects.all()
    return render(request, "seat/seat2.html", {'seats': seats})

@login_required
@csrf_exempt
def view_seat(request, seat_id):

    # result = braintree.Transaction.sale({
    # "amount": "234.00",
    # "credit_card": {
    #     "number": "4111111111111111",
    #     "expiration_month": "05",
    #     "expiration_year": "2016"
    # }
    # })
    #
    # if result.is_success:
    #     print("success!: " + result.transaction.id)
    # elif result.transaction:
    #     print("Error processing transaction:")
    #     print("  message: " + result.message)
    #     print("  code:    " + result.transaction.processor_response_code)
    #     print("  text:    " + result.transaction.processor_response_text)
    # else:
    #     print("message: " + result.message)
    #     for error in result.errors.deep_errors:
    #         print("attribute: " + error.attribute)
    #         print("  code: " + error.code)
    #         print("  message: " + error.message)

    seat = Seat.objects.get(id=seat_id)
    data = {'seat': seat}
    return render(request, "seat/view_seat2.html", data)

@login_required
@csrf_exempt
def add_seat(request):
    if request.method == "POST":
        form = SeatForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/seat")
    else:
        form = SeatForm()
    data = {'form': form}
    return render(request, "seat/add_seat2.html", data)

@login_required
@csrf_exempt
def form(request):
    return render_to_response("braintree.html", {}, context_instance=RequestContext(request))

@csrf_exempt
def thank_you(request):
    return render_to_response("thank_you.html")

@csrf_exempt
def error(request):
    return render_to_response("error.html")

@csrf_exempt
def create_transaction(request):

    if request.method == "POST":
        result = braintree.Transaction.sale({
            "amount": "9.75",
            "credit_card": {
                "number": request.POST.get("number"),
                "cvv": request.POST.get("cvv"),
                "expiration_month": request.POST.get("month"),
                "expiration_year": request.POST.get("year"),
            },
            "options": {
                "submit_for_settlement": True
            }
        })
        if result.is_success:
            user = request.user
            user.paid = True
            user.save()
            return redirect("/thank_you/")
        else:
            return redirect("/error/")


