from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]