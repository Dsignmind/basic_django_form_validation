from django import forms
from django.core import validators


###This is an example of how to do manual validation checking
#############################################################
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                 widget=forms.HiddenInput)
    

    
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Bot Detected!')
    #     return botcatcher


# ##example of custom validator function
# #######################################
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.validators("Name should start with a 'z'!")

#     ###Validation using Django form built-ins
# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                 widget=forms.HiddenInput,
#                                 validators=[validators.MaxLengthValidator(0)])


###Example of doing one time form validation
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label='Verify email:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        if all_clean_data['email'] != all_clean_data['verifyEmail']:
            raise forms.ValidationError('The emails you entered are not the same!')
