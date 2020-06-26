from django.urls import path
from . import views
from ATN.settings import DEBUG,STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-toy'),
    path('update/<int:toy_id>', views.update_toy),
    path('delete/<int:toy_id>', views.delete_toy),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
