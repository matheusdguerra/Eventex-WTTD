from django.contrib import admin
from django.urls import include, path
import eventex.core.views

urlpatterns = [
    path('', eventex.core.views.home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls')),
    path('admin/', admin.site.urls),
]
