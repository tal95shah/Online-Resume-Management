from accounts import models
class ResumeForm(forms.ModelForm):


    class Meta:
        model = models.Profile
        fields = [
            'applicant'
            'job',
            'internship',
            'current_employer',
            'current_designation',
            'current_organization_experience',
            'objective',
            'department',
            'skills',
            'min_salary',
            'extra_curricular',
            'other_interests'
        ]