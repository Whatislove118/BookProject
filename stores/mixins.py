from stores.models import Pizzeria
from stores.serializers import PizzeriaDetailSerializer


class QuerysetSerializerMixin:
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer