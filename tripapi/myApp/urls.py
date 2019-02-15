from django.conf.urls import url
from .views import UsersView, TripsView, EditTripsView, DeleteTripsView

app_name = "myApp"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url(r'users/$', UsersView.as_view()),
    url(r'trips/$', TripsView.as_view()),
    url(r'edit/(?P<pk>[0-9]+)/$', EditTripsView.as_view()),
    url(r'delete/(?P<pk>[0-9]+)/$', DeleteTripsView.as_view()),
]
