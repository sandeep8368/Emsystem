from django.urls import path
from emp.views import EmployeeListCreate,EmployeeRetrieveUpdateDestroy

urlpatterns = [
    path('employee/', EmployeeListCreate.as_view(),name='Employee-List-Create'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(),name='Employee-List-Create'),
]
