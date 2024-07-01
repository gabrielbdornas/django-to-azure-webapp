from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sinhala_translator_dashboard/', views.sinhala_translator_dashboard, name='sinhala_translator_dashboard'),
    path('tamil_translator_dashboard/', views.tamil_translator_dashboard, name='tamil_translator_dashboard'),
    path('illustrator_dashboard/', views.illustrator_dashboard, name='illustrator_dashboard'),
    path('sinhala_edit/<int:question_id>/', views.sinhala_editing_interface, name='sinhala_editing_interface'),
    path('tamil_edit/<int:question_id>/', views.tamil_editing_interface, name='tamil_editing_interface'),
    path('illustrator_edit/<int:question_id>/', views.illustrator_editing_interface, name='illustrator_editing_interface'),
    path('delete_image/', views.delete_image, name='delete_image'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
