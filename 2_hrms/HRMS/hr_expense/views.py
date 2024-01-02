from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from hr_expense.models import ExpenseModel
from hr_expense import forms


class expense_detail(DetailView):
    model = ExpenseModel
    context_object_name = "expense"
    template_name = 'expense_detail.html'


class expense_list(ListView):
    model = ExpenseModel
    context_object_name = 'all_expenses'
    template_name = 'expense_list.html'


class expense_add(CreateView):
    success_url = reverse_lazy("expense_list")
    model = ExpenseModel
    form_class = forms.ExpenseForm
    template_name = 'expense_create.html'


class expense_update(UpdateView):
    model = ExpenseModel
    template_name = 'expense_update.html'
    fields = [
        'name',
        'date',
        'category',
        'description',
        'reason',

        'claimed_amount',
        'approved_amount',
        'currency',
        'payment_name',
        'payment_description',

        'payment_date',
        'claimed_date',
        'approval_date',
        'receipt_image',
        'status',

        'comments',
        'note'
    ]
    success_url = reverse_lazy("expense_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the document instance to the context
        context['receipt_image'] = self.object
        return context

    def form_valid(self, form):
        # Delete the old file if it exists
        instance = form.instance
        if instance.pk:
            old_instance = ExpenseModel.objects.get(pk=instance.pk)
            old_instance.receipt_image.delete(save=False)
            # Delete the old file without saving changes to the database

        # Save the new file
        return super().form_valid(form)


class expense_delete(DeleteView):
    def get(self, request, pk):
        expense = ExpenseModel.objects.get(id=pk)
        expense.delete()
    success_url = reverse_lazy("expense_list")