from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('index_author', views.index_author),
    path('new_book', views.new_book),
    path('new_author', views.new_author),
    path('display_book/<int:id>', views.display_book),
    path('display_author/<int:id>', views.display_author),
    path('add_book_to_list', views.add_book_to_list),
    path('add_author_to_list', views.add_author_to_list),
]