from django.urls import path
from stores.views import PizzeriaListAPIView, PizzeriaDetailAPIView, PizzeriaCreateAPIView, \
    PizzeriaRetrieveUpdateAPIView, PizzeriaDestroyAPIView

urlpatterns = [
    path('', PizzeriaListAPIView.as_view(), name='pizzeria_list'),
    path('<int:id>/', PizzeriaDetailAPIView.as_view(), name='pizzeria_detail'),
    path('create/', PizzeriaCreateAPIView.as_view(), name='pizzeria_create'),
    path('update/<int:id>/', PizzeriaRetrieveUpdateAPIView.as_view(), name='pizzeria_update'),
    path('delete/<int:id>/', PizzeriaDestroyAPIView.as_view(), name='pizzeria_destroy')
]