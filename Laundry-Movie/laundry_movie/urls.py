from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('dumpdata/', include('dumpData.urls')),
    path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('dj_rest_auth.urls')),
    # path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    #path('<username>/', accounts_views.people, name="people"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)