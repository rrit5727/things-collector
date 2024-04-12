from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view() ,name='dogs_create' ),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update' ),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete' ),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('dogs/<int:dog_id>/assoc_park/<int:park_id>/', views.assoc_park, name="assoc_park"),
    path('parks/', views.ParkList.as_view(), name='parks_list'),
    path('parks/<int:pk>/', views.ParkDetail.as_view(), name='parks_detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='parks_create'),
    path('parks/<int:pk>/update/', views.ParkUpdate.as_view(), name='parks_update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='parks_delete'),
    path('accounts/signup/', views.signup, name="signup"),
]