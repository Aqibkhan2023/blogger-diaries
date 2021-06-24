from django.contrib import admin
from django.urls import path, include
from froala_editor import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls')),
]
