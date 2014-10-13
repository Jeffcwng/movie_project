from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movie_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movie_app.views.home', name='home'),
    url(r'^about/$', 'movie_app.views.about', name='about'),
    url(r'^contact/$', 'movie_app.views.contact', name='contact'),
    url(r'^movie_ajax/$', 'movie_app.views.movie_ajax', name='movie_ajax'),
    url(r'^showtime_ajax/$', 'movie_app.views.showtime_ajax', name='showtime_ajax'),
    url(r'^buyticket/$', 'movie_app.views.buyticket', name='buyticket'),

    # register log in and out
    url(r'^profile/$', 'movie_app.views.profile', name='profile'),
    url(r'^register/$', 'movie_app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    #password reset
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^movie/$', 'movie_app.views.movie', name='movie'),
    url(r'^movie/add/$', 'movie_app.views.add_movie', name='add_movie'),
    url(r'^movie/(?P<movie_id>\w+)/$$', 'movie_app.views.view_movie', name='view_movie'),

    url(r'^showtime/$', 'movie_app.views.showtime', name='showtime'),
    url(r'^showtime/add/$', 'movie_app.views.add_showtime', name='add_showtime'),
    url(r'^showtime/(?P<showtime_id>\w+)/$$', 'movie_app.views.view_showtime', name='view_showtime'),

    url(r'^seat/$', 'movie_app.views.seat', name='seat'),
    url(r'^seat/add/$', 'movie_app.views.add_seat', name='add_seat'),
    url(r'^seat/(?P<seat_id>\w+)/$$', 'movie_app.views.view_seat', name='view_seat'),

    ##### for braintree
    url(r'^create_transaction/$', 'movie_app.views.create_transaction', name='create_transaction'),
    url(r'^payment/$', 'movie_app.views.form', name='payment'),
    url(r'^thank_you/$', 'movie_app.views.thank_you', name='thank_you'),
    url(r'^error/$', 'movie_app.views.error', name='error'),


)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)