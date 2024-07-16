from django.urls import path
from apps.gallery.views import index, image, search, add_image, edit_image, delete_image, filter

urlpatterns = [
  path('', index, name='index'),
  path('image/<int:picture_id>', image, name='image'),
  path('search', search, name='search'),
  path('add-image', add_image, name='add_image'),
  path('edit-image/<int:picture_id>', edit_image, name='edit_image'),
  path('delete-image/<int:picture_id>', delete_image, name='delete_image'),
  path('filter/<str:category>', filter, name='filter')
]