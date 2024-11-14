from django.urls import path
from .views import BookListView, BookDetailView,BookDeleteView,BookUpdateView

urlpatterns = [
    path('api/book/', BookListView.as_view(), name='book_list'),
    path('api/book/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    path('api/book/delete/<int:book_id>/', BookDeleteView.as_view(), name='book_delete'),
    path('api/book/update/<int:book_id>/', BookUpdateView.as_view(), name='book_update')


    
]
