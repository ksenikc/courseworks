from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .filters import PostFilter
from .models import  Stat,Orders
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils import timezone
from .models import Product, Reviews


def home(request):
    tasks_all = Product.objects.order_by('id')
    posts = PostFilter(request.GET, queryset=tasks_all)
    context = {
        'posts': posts,
        'title':"Главная страница",

    }
    return render(request, 'blog/home.html', context)


class ProductDetailView(DetailView):
    model = Product


def record(request):
    data = Reviews.objects.all()

    context = {
        'reviews': data
    }
    return render(request, 'blog/record.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Reviews
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserProductListView(ListView):
    model = Product
    context_object_name = 'products'
    now = timezone.now()
    extra_context = {'title': 'История записей', 'now': now}


class UserOrdersListView(ListView):
    model = Orders
    context_object_name = 'orders'
    now = timezone.now()
    extra_context = {'title': 'История записей', 'now': now}

    def get_queryset(self):
        return Orders.objects.filter(owner=self.request.user).order_by('-created')

class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'blog/orders_forms.html'
    success_url = '/'

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'В поле {field} возникла ошибка: {error}')
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        print(self.request)
        print(self.kwargs['pk'])
        form.instance.stat = Stat.objects.get(id=2)  # Отправлен
        form.instance.prod = Product.objects.get(id=self.kwargs['pk'])  # Выбираем товар по pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['header_text'] = "My Form"
        pk = self.kwargs.get('pk')
        selected_product = Product.objects.get(id=pk)
        context['prod_info'] = f'Наименование: {selected_product.title} '
        return context

def ajax_change_status(request, pk):
    order_id = request.GET.get('id', False)
    status = Stat.objects.get(id=3)
    number = Orders.objects.filter(id=pk).update(stat=status)
    return redirect('orders-list', username=request.user)
