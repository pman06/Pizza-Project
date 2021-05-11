from django.urls import path
from stores import views

app_name = 'pizzeria'

urlpatterns = [
    path('', views.PizzeriaListAPIView.as_view(), name='pizzeria_list'),
    path(
        '<int:id>/',
        views.PizzeriaRetrieveAPIView.as_view(),
        name='pizzeria_detail'
    ),
    path('create/',
         views.PizzeriaCreateAPIView.as_view(),
         name='pizzeria_create'
         ),
    path(
        'update/<int:id>/',
        views.PizzeriaUpdateAPIView.as_view(),
        name='pizzeria_update'
    ),
    path(
        'delete/<int:id>/',
        views.PizzeriaDeleteAPIView.as_view(),
        name='pizzeria_delete'
    ),
]
