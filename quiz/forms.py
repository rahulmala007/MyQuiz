from django.db import models
from django.forms import ModelForm
from .models import *
from django import forms
DATE_INPUT_FORMATS = ('%d/%m/%Y','%Y/%m/%d')
class mDateInput(forms.DateInput):
    input_type = 'date'

class mTimeInput(forms.TimeInput):
    input_type= 'time'

class QuizForm(ModelForm):
    
    # start_date= forms.DateField(input_formats=DATE_INPUT_FORMATS)
    # start_time= forms.TimeField()
    # end_date= forms.DateField(input_formats=DATE_INPUT_FORMATS)
    # end_time= forms.TimeField()
    class Meta:
        model=quiz
        fields=['title','description','random_order_required','start_date','start_time','end_date','end_time','duration']
        widgets = {

        'start_date': mDateInput(),
        'start_time': mTimeInput(),
        'end_date': mDateInput(),
        'end_time': mTimeInput()

        }





