from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import CategoryFilter
from .forms import UpdateCategoryForm
from .models import Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ["name", "type"]
    template_name = "category/category_add.html"
    success_url = "category-home"

    def form_valid(self, form):
        category = form.save(commit=False)
        category.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class CategoryListView(ListView):
    paginate_by = 10
    queryset = Category.objects.all()
    template_name = "category/category_home_page.html"
    context_object_name = "categories"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CategoryFilter(self.request.GET, queryset=queryset)

        if not self.filterset.qs.query.order_by:
            queryset = self.filterset.qs.order_by("-name")
        else:
            queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if Category.objects.filter(user_id=self.request.user):
            return context


class CategoryUpdateView(UpdateView):
    model = Category
    form = UpdateCategoryForm
    fields = ["name", "type"]
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
