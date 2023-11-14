from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Earning, Package, Course, Payment, PackageTaken
from .serializer import EarningSerializer
from django.contrib.auth import get_user_model
import collections
from .forms import CourseForm
import razorpay

User = get_user_model()

# Create your views here.


@api_view(["GET"])
def getData(request):
    earned = Earning.objects.all().order_by('-earned')
    top_earned = earned[:10]
    serializer = EarningSerializer(earned, many=True)
    top_users = serializer.data
    for i in range(len(earned)):
        top_users[i] = collections.OrderedDict(top_users[i])
        username = ('username', top_earned[i].user.get_username())
        items = list(top_users[i].items())
        items.append(username)
        try:
            image = ('image', top_earned[i].user.profile_image.url)
            items.append(image)
        except Exception:
            items.append(('image', ""))
        items.sort()
        top_users[i] = collections.OrderedDict(items)
    return Response(top_users)


def manage_site(request):
    form = CourseForm()
    context = {
        "form": form
    }
    return render(request, 'admin/manage_site.html', context)


def view_package(request, slug):
    queryset = Package.objects.get(slug=slug)
    context = {
        'package': queryset
    }
    if request.user.is_authenticated:
        key_id = "rzp_test_JhJ7T29B0KtFsM"
        key_secret = "3VcIs3MI0gRNVenMNq7S2ybk"
        client = razorpay.Client(auth=(key_id, key_secret))
        payment = client.order.create({'amount': queryset.price*100, 'currency': 'INR', 'payment_capture': 1})
        user = User.objects.get(id=request.user.id)
        try:
            p = Payment.objects.get(user=user)
            p.order_id = payment['id']
            p.save()
        except Exception:
            p = Payment.objects.create(user = user, order_id=payment['id'], is_success=False)
            p.save()
        context['payment'] = payment
        context['p'] = p
    return render(request, 'course/view_package.html', context)


def add_package(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        desc = request.POST.get('desc')

        package = Package.objects.create(name=name, price=price, image=image, description = desc)
        package.save()
        return redirect('manage-site')


def add_course(request):
    if request.method == 'POST':
        p = request.POST.get('package')
        name = request.POST.get('name')
        about = request.POST.get('about')
        package = Package.objects.get(id=p)

        course = Course.objects.create(package=package, name=name, about=about)
        course.save()
        return redirect('manage-site')


def payment_success(request):
    order_id = request.GET.get('order_id')
    package_id = request.GET.get('package_id')
    p = Payment.objects.get(order_id=order_id)
    p.is_success = True
    p.save()
    user = User.objects.get(id=request.user.id)
    package = Package.objects.get(id=package_id)
    try:
        pt = PackageTaken.objects.get(user=user)
        pt.package = package
        pt.save()
    except Exception:
        pt = PackageTaken.objects.create(user=user, package=package)
        pt.save()
    return redirect('dashboard')
