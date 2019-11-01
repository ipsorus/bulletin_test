from django.urls import path

from bulletin.views import redirect_main_page

from user_modal import views
from bulletin_board import urls


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),
    path('read/<int:pk>', views.BookReadView.as_view(), name='read_book'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete_book'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]