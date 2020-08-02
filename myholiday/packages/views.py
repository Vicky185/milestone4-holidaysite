from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Package, Category

# Create your views here.
def all_packages(request):
    """ a view to show all of the available holidays, includes sorting and search queries"""

    packages = Package.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    packages = packages.annotate(lower_name=Lower('name'))

                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                packages = packages.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            packages = packages.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria...")
                return redirect(reverse('packages'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            packages = packages.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'packages': packages,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'packages/packages.html', context)

def one_package_detail(request, package_id):
    """ a view to show individual package with more detail and description """
    package = get_object_or_404(Package, pk=package_id)

    context_detail = {
        'package': package,
    }

    return render(request, 'packages/one_package_detail.html', context_detail)