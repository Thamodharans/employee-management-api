from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend # type: ignore

from .models import Employee
from .serializers import EmployeeSerializer
from .pagination import EmployeePagination

class EmployeeViewSet(ModelViewSet):
    """
    Employee CRUD API with:
    - JWT authentication
    - Pagination
    - Filtering by department and role
    - Search by name and email
    """
    queryset = Employee.objects.all().order_by('-date_joined')  # newest first
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination
    permission_classes = [IsAuthenticated]

    # Enable filtering & search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['department', 'role']  # fields must exist in the model
    search_fields = ['name', 'email']


