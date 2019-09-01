from django.conf.urls import url
from pages.views import index, about_page, logout, login, registration, customer_profile

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about$', about_page, name="about_page"),
    url(r'^pages/logout/$', logout, name="logout"),
    url(r'^pages/login/$', login, name="login"),
    url(r'^pages/register/$', registration, name="registration"),
    url(r'^accounts/profile/$', customer_profile, name="profile")
]

