from django.conf.urls import url
from pages.views import index, about_page, logout, login, registration, customer_profile

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about/$', about_page, name="about_page"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', customer_profile, name="profile")
]

