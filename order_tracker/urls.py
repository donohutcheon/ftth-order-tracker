#from django.contrib import admin
from django.urls import path
from .views import ListInstallationsView, CreateInstallationView


urlpatterns = [
#    path('admin/', admin.site.urls),
    path('installations/', ListInstallationsView.as_view(), name="installations-all"),
    path('create/installation/', CreateInstallationView.as_view(), name="create-installation")
]
