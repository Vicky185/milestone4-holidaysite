from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Package, Category, Comment
from .forms import PackageForm, CommentForm


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
                if sortkey == 'category':
                    sortkey = 'category__name'
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

    # List of comments for this post
    comments = package.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment is or was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create a comment object but don't save to database just yet
            new_comment = comment_form.save(commit=False)
            # Assign the current package to the comment
            new_comment.package = package
            # Save the comment to database
            new_comment.save()
            messages.success(request, 'Successfully added your comment/review!')
            return redirect(reverse('one_package_detail', args=[package.id]))
        else:
            messages.error(request, 'Failes to add your comment to this package. Please ensure the form is valid.')
    else:
        comment_form = CommentForm()

    template = 'packages/one_package_detail.html'
    context_detail = {
        'package': package,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, template, context_detail)

@login_required
def add_package(request):
    """ Add a package to the available holidays """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only members of the MyHoliday travels team can do that...')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()
            messages.success(request, 'Successfully added the new travel package!')
            return redirect(reverse('one_package_detail', args=[package.id]))
        else:
            messages.error(request, 'Failed to add the new package. Please ensure the form is valid.')
    else:
        form = PackageForm()

    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_package(request, package_id):
    """ Edit an existing available travel package  """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only members of the MyHoliday travels team can do that...')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated package!')
            return redirect(reverse('one_package_detail', args=[package.id]))
        else:
            messages.error(request, 'Failed to update the package. Please ensure that the form is valid.')
    else:
        form = PackageForm(instance=package)
        messages.info(request, f'You are currently editing {package.name}')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)

@login_required
def delete_package(request, package_id):
    """ Delete an existing available travel package  """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only members of the MyHoliday travels team can do that...')
        return redirect(reverse('home'))
        
    package = get_object_or_404(Package, pk=package_id)
    package.delete()
    messages.success(request, 'Package deleted!')
    return redirect(reverse('packages'))

