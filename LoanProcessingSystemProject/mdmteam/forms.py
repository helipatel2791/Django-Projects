from django import forms

class TestForm(forms.Form):

    # HTMl INPUT Box
    LoanID = forms.IntegerField()
    CreditScoreMin = forms.IntegerField(required=False)
    CreditScoreMax = forms.IntegerField(required=False)
    LoanAmountMin = forms.IntegerField(required=False)
    LoanAmountMax = forms.IntegerField(required=False)
    IntrestRatePct = forms.IntegerField(required=False)
    DurationMonths = forms.IntegerField(required=False)
    eff_from_date = forms.IntegerField(required=False) #forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), input_formats=('%m/%d/%Y', )) # widget=) # forms.IntegerField()
    eff_to_date = forms.IntegerField(required=False) #forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), input_formats=('%m/%d/%Y', )) # ) # forms.IntegerField()

class EditForm(forms.Form):

    LoanID = forms.IntegerField()#(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    CreditScoreMin = forms.IntegerField(required=False)
    CreditScoreMax = forms.IntegerField(required=False)
    LoanAmountMin = forms.IntegerField(required=False)
    LoanAmountMax = forms.IntegerField(required=False)
    IntrestRatePct = forms.IntegerField(required=False)
    DurationMonths = forms.IntegerField(required=False)
    eff_from_date = forms.IntegerField(required=False) #forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), input_formats=('%m/%d/%Y', )) # widget=) # forms.IntegerField()
    eff_to_date = forms.IntegerField(required=False)
    
