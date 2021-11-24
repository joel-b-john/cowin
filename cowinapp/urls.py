from django.urls import path

from cowinapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('book/',views.book,name='book'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('views/',views.views,name='views'),
    path('logout/',views.logout,name='logout'),
    path('token/',views.token,name='token'),
]