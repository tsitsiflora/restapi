from django.conf.urls import url
from .views import ListUsersView, ListTripsView

app_name = "myApp"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url(r'users/', ListUsersView.as_view()),
    url(r'trips/', ListTripsView.as_view()),
]

