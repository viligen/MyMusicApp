from django.urls import path

from examproject.exam.views import index, add_item, details_item, edit_item, delete_item, delete_profile, \
    details_profile

urlpatterns = [
    path('', index, name='index'),
    path('album/add/', add_item, name='add item'),
    path('album/details/<id>/', details_item, name='details item'),
    path('album/edit/<id>/', edit_item, name='edit item'),
    path('album/delete/<id>/', delete_item, name='delete item'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

]