class update(UpdateView):
    model = models.ResumeModel
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
    uploaded_file = form.cleaned_data['resume']
    print("Uploaded File:", uploaded_file)
    return super().form_valid(form)
