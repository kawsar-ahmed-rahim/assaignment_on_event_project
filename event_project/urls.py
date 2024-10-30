from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home,name="homepage"),
path('category/', include("categories.urls")),
path('event/', include("events.urls")),
path('registration/', include("registration.urls")),
path('login_logout/', include("login_logout.urls")),
path('user_profile/', include("user_profile.urls")),
path('booked_events/', include("booked_events.urls")),

]

