from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method =='POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('validation success')
            submittedData = form.cleaned_data
            print('You entered:\nName: {0}\nEmail: {1}\nMessage: {2}'.format(submittedData['name'],submittedData['email'], submittedData['text']))
    return render(request, 'basicapp/form_page.html', {'form': form})