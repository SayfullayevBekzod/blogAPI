from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'


class My10NumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
