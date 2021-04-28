from django import forms


class CritForm(forms.Form):
    category = forms.ChoiceField(label='Critical Category', choices=(('M', 'Magic'), ('S', 'Slashing'), ('P', 'Piercing'), ('B', 'Bludgeoning')))
    severity = forms.ChoiceField(label='Critical Severity', choices=(('E', 'Extreme'), ('M', 'Moderate'), ('W', 'Mild')))
    success = forms.ChoiceField(label='Critical Type', choices=(('T', 'Success'), ('F', 'Fail')))
    flavor_text = forms.CharField(label='Critical Text', max_length=1000)

