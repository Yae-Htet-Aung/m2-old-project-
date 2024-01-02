from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from hr_recruitment.models import ResumeModel
from hr_recruitment import forms
import os
from django.conf import settings
from django.shortcuts import redirect, render


class resume_detail(DetailView):
    model = ResumeModel
    context_object_name = "resume"
    template_name = 'resume_detail.html'


class resume_list(ListView):
    print('resume_list called ***')
    model = ResumeModel
    context_object_name = 'all_resumes'
    template_name = 'resume_list.html'


class resume_add(CreateView):
    print('resume_add called *** ')
    success_url = reverse_lazy("resume_list")
    model = ResumeModel
    form_class = forms.ResumeForm
    template_name = 'resume_create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the document instance to the context
        context['resume'] = self.object
        return context


class resume_update(UpdateView):
    print('resume_update called *** ')
    success_url = reverse_lazy("resume_list")
    model = ResumeModel
    template_name = 'resume_update.html'
    context_object_name = "resume"
    # form_class = forms.ResumeForm
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the document instance to the context
        context['resume'] = self.object
        return context
    
    def form_valid(self, form):
        # print("form valid *** ")
        # Delete the old file if it exists
        instance = form.instance
        if instance.pk:
            old_instance = ResumeModel.objects.get(pk=instance.pk)
            old_instance.resume.delete(save=False) # Delete the old file without saving changes to the database
            # print('old file deleted *** ')
        # Save the new file
        if self.object.resume:
            # print('new file check *** ', self.object.resume)
            # Delete the old file if it exists
            if self.object.resume.name:
                # print('self.object.resume.name ***', self.object.resume.name)
                old_file_path = self.object.resume.path
                if os.path.isfile(old_file_path):
                    os.remove(old_file_path)
        return super().form_valid(form)
    
    
class resume_delete(DeleteView):
    success_url = reverse_lazy('resume_list')
    model = ResumeModel
    context_object_name = "resume"
    template_name = 'resume_delete.html' 
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object() # Get the model instance to delete

        if instance.resume: # Delete the related file from the media directory
            file_path = os.path.join(settings.MEDIA_ROOT, str(instance.resume))
            if os.path.exists(file_path):
                os.remove(file_path)

        # Delete the model instance
        return super().delete(request, *args, **kwargs)