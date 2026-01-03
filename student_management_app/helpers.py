"""
Pagination and search helpers
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def paginate_queryset(queryset, request, items_per_page=10):
    """
    Paginate a queryset
    
    Args:
        queryset: Django queryset to paginate
        request: HTTP request object
        items_per_page: Number of items per page
    
    Returns:
        Tuple of (page_obj, paginator)
    """
    paginator = Paginator(queryset, items_per_page)
    page_number = request.GET.get('page', 1)
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return page_obj, paginator


def search_queryset(queryset, search_query, search_fields):
    """
    Search a queryset across multiple fields
    
    Args:
        queryset: Django queryset to search
        search_query: Search string
        search_fields: List of field names to search
    
    Returns:
        Filtered queryset
    """
    if not search_query or not search_fields:
        return queryset
    
    # Build Q objects for OR search
    query = Q()
    for field in search_fields:
        query |= Q(**{f"{field}__icontains": search_query})
    
    return queryset.filter(query)


def get_pagination_context(page_obj, request):
    """
    Get context data for pagination template
    
    Args:
        page_obj: Page object from paginator
        request: HTTP request object
    
    Returns:
        Dictionary with pagination context
    """
    # Get query parameters except page
    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']
    query_string = query_params.urlencode()
    
    context = {
        'page_obj': page_obj,
        'query_string': query_string,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'page_number': page_obj.number,
        'total_pages': page_obj.paginator.num_pages,
        'start_index': page_obj.start_index(),
        'end_index': page_obj.end_index(),
        'total_count': page_obj.paginator.count,
    }
    
    # Add page range for navigation
    page_range = []
    current_page = page_obj.number
    total_pages = page_obj.paginator.num_pages
    
    # Show first page
    if current_page > 3:
        page_range.append(1)
        if current_page > 4:
            page_range.append('...')
    
    # Show pages around current
    for i in range(max(1, current_page - 2), min(total_pages + 1, current_page + 3)):
        page_range.append(i)
    
    # Show last page
    if current_page < total_pages - 2:
        if current_page < total_pages - 3:
            page_range.append('...')
        page_range.append(total_pages)
    
    context['page_range'] = page_range
    
    return context
