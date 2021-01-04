from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart, chart, text1


urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('chartbydate/<int:year>/<int:month>/',chart),
    path('chartbydate/<int:year>/',chart),
    path('text1/<str:slug>/', text1),
    path('', homepage),
]