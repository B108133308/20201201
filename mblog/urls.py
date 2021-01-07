from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart, chart, Text1, citykeep, cityhuman, cityadopt, citydied


urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('chartbydate/<int:year>/<int:month>/',chart),
    path('chartbydate/<int:year>/',chart),
    path('text1/', Text1),
    path('keep/', citykeep),
    path('keep/<int:bid>/', citykeep),
    path('human/', cityhuman),
    path('human/<int:bid>/', cityhuman),
    path('adopt/', cityadopt),
    path('adopt/<int:bid>/', cityadopt),
    path('died/', citydied),
    path('died/<int:bid>/', citydied),
    path('', homepage),
]