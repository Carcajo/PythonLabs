from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from cart.forms import CartAddProductForm

from .forms import LoginUserForm, RegisterUserForm
from .models import Product

# Create your views here.


class AllProducts(ListView):
    model = Product
    extra_context = {"title": "Products"}


# class HomePage()


def index(request):
    context = {"title": "JoService"}
    return render(request, "gshop/index.html", context=context)


def about(request):
    context = {
        "title": "About service",
    }
    return render(request, "gshop/about.html", context=context)


class CatProducts(ListView):
    model = Product
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_selected"] = context["object_list"][0].category_id
        context["title"] = str(context["object_list"][0].category)
        return context

    def get_queryset(self):
        return Product.objects.filter(
            category__slug=self.kwargs["category_slug"], is_available=True
        )


class UnoProduct(DetailView):
    model = Product
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_form"] = CartAddProductForm()
        context["title"] = str(context["object"].name)
        return context

    def get_queryset(self):
        return Product.objects.filter(
            category__slug=self.kwargs["category_slug"],
            slug=self.kwargs["product_slug"],
            is_available=True,
        )


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "gshop/register.html"
    success_url = reverse_lazy("login")
    extra_context = {"title": "Registration"}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("all_products")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "gshop/login.html"
    extra_context = {"title": "Registration"}


def logout_user(request):
    logout(request)
    return redirect("home")
