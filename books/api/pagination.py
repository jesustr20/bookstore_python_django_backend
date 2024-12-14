from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10  # Tamaño por defecto
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        # Verifica si no hay registros en la página actual
        response = {
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
        }

        # Excluir 'next' y 'previous' si no hay más de una página
        if self.page.paginator.num_pages > 1:
            response['next'] = self.get_next_link()
            response['previous'] = self.get_previous_link()

        return Response(response)