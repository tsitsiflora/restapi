from django.conf.urls import url
from .views import UsersView, TripsView, EditTripsView, DeleteTripsView, DeleteUsersView, PostUsersView, PostTripsView

app_name = "myApp"


urlpatterns = [
    url(r'users/$', UsersView.as_view()),
    url(r'postuser/$', PostUsersView.as_view()),
    url(r'trips/$', TripsView.as_view()),
    url(r'posttrip/$', PostTripsView.as_view()),
    url(r'edit/(?P<pk>[0-9]+)/$', EditTripsView.as_view()),
    url(r'deletetrip/(?P<pk>[0-9]+)/$', DeleteTripsView.as_view()),
    url(r'deleteuser/(?P<pk>[0-9]+)/$', DeleteUsersView.as_view())
]

