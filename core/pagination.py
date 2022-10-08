from rest_framework import pagination

# 공통 페이징 클래스


class DefaultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
