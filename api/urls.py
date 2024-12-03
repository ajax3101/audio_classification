from django.urls import path
from .views import AudioUploadView, ESC50MetadataListView, home_view

urlpatterns = [
    path('upload/', AudioUploadView.as_view(), name='audio-upload'),
    path('metadata/', ESC50MetadataListView.as_view(), name='metadata-list'),
    path('', home_view, name='home'),

]