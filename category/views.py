from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UpdateCategoryForm
from .models import Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ["category_name", "category_type"]
    template_name = "category/category_add.html"
    success_url = "category-home"

    def form_valid(self, form):
        category = form.save(commit=False)
        category.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class CategoryListView(ListView):
    model = Category
    template_name = "category/category_home_page.html"
    context_object_name = "categories"
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
    success_url = "category-home"

    def get_queryset(self):
        return Category.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/category_delete.html"
    success_url = "category-home"

    def get_queryset(self):
        return Category.objects.filter(user_id_id=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
