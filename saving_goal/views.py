from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import SavingGoalFilter
from .forms import CreateSavingGoalForm, UpdateSavingGoalForm
from .models import SavingGoal


class SavingGoalCreateView(CreateView):
    model = SavingGoal
    form_class = CreateSavingGoalForm
    template_name = "saving_goal/goal_add.html"
    success_url = "goal-home"

    def form_valid(self, form):
        goal = form.save(commit=False)
        goal.user_id = self.request.user.id
        form.save()

        return redirect(self.success_url)


class SavingGoalListView(ListView):
    paginate_by = 10
    queryset = SavingGoal.objects.all()
    template_name = "saving_goal/goal_home_page.html"
    context_object_name = "goals"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = SavingGoalFilter(self.request.GET, queryset=queryset)

        if not self.filterset.qs.query.order_by:
            queryset = self.filterset.qs.order_by("-target_date")
        else:
            queryset = self.filterset.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        if SavingGoal.objects.filter(user_id=self.request.user):
            return context


class SavingGoalUpdateView(UpdateView):
    model = SavingGoal
    form_class = UpdateSavingGoalForm
    template_name = "saving_goal/goal_update_form.html"
    success_url = "goal-home"

    def get_queryset(self):
        return SavingGoal.objects.filter(user_id=self.request.user)

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class SavingGoalDeleteView(DeleteView):
    model = SavingGoal
    template_name = "saving_goal/goal_delete.html"
    success_url = "goal-home"

    def get_queryset(self):
        return SavingGoal.objects.filter(user_id=self.request.user)

    def form_valid(self, form):
        self.object.delete()

        return redirect(self.success_url)
