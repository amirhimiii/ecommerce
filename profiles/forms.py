from django import forms
from django.contrib.auth import get_user_model


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].disabled = None
        
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['is_author'].disabled = True
            self.fields['is_special'].disabled = True


    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name',
        'is_author','is_special']

