from django.contrib import admin
from django.urls import include, path
from eventex.core.views import home, speaker_detail
#import eventex.core.views

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls')),
    path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]

# 1º -> rota urls
# 2º -> Views com caminho do conteúdo HTML
# 3º -> arquivo html
