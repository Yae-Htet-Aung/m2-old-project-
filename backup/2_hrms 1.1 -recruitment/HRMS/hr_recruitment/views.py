from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from hr_recruitment.models import ResumeModel
from hr_recruitment import forms


class detail(DetailView):
    model = ResumeModel
    context_object_name = "resume"
    template_name = 'resume_detail.html'


class list(ListView):
    model = ResumeModel
    context_object_name = 'all_resumes'
    template_name = 'resume_list.html'


class add(CreateView):
    success_url = reverse_lazy("list")
    model = ResumeModel
    form_class = forms.ResumeForm
    template_name = 'resume_create.html'


class update(UpdateView):
    model = ResumeModel
    template_name = 'resume_update.html'
    fields = [
        'name',
        'submission_date',
        'sequence',
        'appointment_date',
        'resume',
        'interview_date',
        'interview_location',
        'interview_feedback',
        'assessment_score',
        'assessment_feedback',
        'status',
        'note',
        'is_active',
        'created_date',
        'offer_extended',
        'offer_accepted',
        'offer_salary',
        'offer_benefits'
    ]
    success_url = reverse_lazy("list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the document instance to the context
        context['resume'] = self.object
        return context
    
    def form_valid(self, form):
        # Delete the old file if it exists
        instance = form.instance
        if instance.pk:
            old_instance = ResumeModel.objects.get(pk=instance.pk)
            old_instance.resume.delete(save=False)
            # Delete the old file without saving changes to the database

        # Save the new file
        return super().form_valid(form)


class delete(DeleteView):
    success_url = reverse_lazy("list")
    model = ResumeModel
    context_object_name = "resume"
    template_name = 'resume_delete.html'
