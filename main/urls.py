from django.urls import path

from main.views import (add_product_ajax, create_product, delete_product, edit_product, get_product_json,
                        login_user, logout_user, register, show_json,
                        show_json_by_id, show_main, show_xml, show_xml_by_id)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
]