from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination): #Кастомный класс пагинации, наследуемый от PageNumberPagination
    page_size = 5   # Определяет количество элементов на странице
    page_size_query_param = 'page_size'  #Позволяет клиентам указывать размер страницы через параметр запроса page_size.
    max_page_size = 100     # Ограничивает максимальный размер страницы
