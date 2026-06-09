from django.urls import path
from my_app.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_page, name='logout_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('product-list/',product_list,name='product_list'),
    path('add-product/',add_product,name='add_product'),
    path('update-product/<int:p_id>/', update_product, name='update_product'),
    path('delete-product/<int:p_id>/', delete_product, name='delete_product'),
    path('product-details/<int:p_id>/', product_details, name='product_details'),
]