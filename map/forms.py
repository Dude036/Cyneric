from django import forms


class CritForm(forms.Form):
    category = forms.ChoiceField(label='Critical Category', choices=(('Magic', 'Magic'), ('Slashing', 'Slashing'), ('Piercing', 'Piercing'), ('Bludgeoning', 'Bludgeoning')))
    severity = forms.ChoiceField(label='Critical Severity', choices=(('Extreme', 'Extreme'), ('Moderate', 'Moderate'), ('Mild', 'Mild')))
    success = forms.ChoiceField(label='Critical Type', choices=(('Success', 'Success'), ('Fail', 'Fail')))
    flavor_text = forms.CharField(label='Critical Text', max_length=1000)

