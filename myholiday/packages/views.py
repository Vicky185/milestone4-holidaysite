from django.shortcuts import render, get_object_or_404
from .models import Package

# Create your views here.
def all_packages(request):
    """ a view to show all of the available holidays, includes sorting and search queries"""

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)

def one_package_detail(request, package_id):
    """ a view to show individual package with more detail and description """
    package = get_object_or_404(Package, pk=package_id)

    context_detail = {
        'package': package,
    }

    return render(request, 'packages/one_package_detail.html', context_detail)