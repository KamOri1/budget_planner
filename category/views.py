from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import UpdateCategoryForm
from .models import Category


class CategoryHomeView(TemplateView):
    template_name = "category/category_home_page.html"


class CategoryCreateView(CreateView):
    model = Category
    fields = ["category_name", "category_type"]
    template_name = "category/category_add.html"
    success_url = "create_category"

    def form_valid(self, form):
        category = form.save(commit=False)
        category.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class CategoryListView(ListView):
    model = Category
    template_name = "category/category_list.html"
    context_object_name = "categorys"
    ordering = ["-category_name"]

    def get_queryset(self):
        return Category.objects.filter(user_id_id=self.request.user).order_by(
            "-category_name"
        )


class CategoryUpdateView(UpdateView):
    model = Category
    form = UpdateCategoryForm
    fields = ["category_name", "category_type"]
    template_name = "category/category_update_form.html"
    success_url = "category_list"

    def get_queryset(self):
        return Category.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url, q="edit")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/category_delete.html"
    success_url = "category_list"

    def get_queryset(self):
        return Category.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url, q="del")
