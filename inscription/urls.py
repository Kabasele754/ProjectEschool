from django.urls import path
from .views import index_view,connect_view,inscription,add,update,delete

urlpatterns = [
    path('',index_view),
    path('connexion/',connect_view, name='connexion'),
    path('inscription/',inscription, name='inscription'),
    path('add/',add, name='add'),
    path('update/<int:id>/',update, name='update'),
    path('delete/<int:id>/',delete, name='delete')
]