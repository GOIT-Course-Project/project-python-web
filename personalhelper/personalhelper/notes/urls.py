from django.urls import path
from django.conf.urls import include, url 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.NoteListView.as_view(), name = 'notes'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('tags/', views.TagListView.as_view(), name = 'tags'),
    path('tags/<int:pk>', views.TagDetailView.as_view(), name='tag-detail'),
]

urlpatterns += [
    path('notes/create/', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
]