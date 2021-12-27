from django.urls import path
from .views import index_view,connect_view,inscription,update,delete

urlpatterns = [
    path('',index_view),
    path('connexion',connect_view, name='connexion'),
    path('inscription',inscription, name='inscription'),
    path('update/<int:id>',update, name='update'),
    path('delete/<int:id>',delete, name='delete')
]