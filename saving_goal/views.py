from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

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
    model = SavingGoal
    template_name = "saving_goal/goal_home_page.html"
    context_object_name = "goals"
    ordering = ["-name"]

    def get_queryset(self):
        return SavingGoal.objects.filter(user_id=self.request.user).order_by("-name")


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
