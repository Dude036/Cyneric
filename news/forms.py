from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(required=True, strip=True, max_length=50)
    article = forms.CharField(required=True, widget=forms.Textarea)

    day = forms.IntegerField(required=True, min_value=1, max_value=28)
    month = forms.ChoiceField(required=True, choices=[
        ('Genysi', 'Genysi'),
        ('Tixyl', 'Tixyl'),
        ('Rysumas', 'Rysumas'),
        ('Anthys', 'Anthys'),
        ('Perigree', 'Perigree'),
        ('Ekarpo', 'Ekarpo'),
        ('Ludere', 'Ludere'),
        ('Therismo', 'Therismo'),
        ('Chima', 'Chima'),
        ('Skotad', 'Skotad'),
        ('Apogee', 'Apogee'),
        ('Pagos', 'Pagos')
    ])
    year = forms.IntegerField(required=True, min_value=1, max_value=100)
    era = forms.ChoiceField(required=True, choices=[
        ('Uniting', 'Uniting'),
        ('Trade', 'Trade'),
        ('Expansion', 'Expansion'),
        ('Magic', 'Magic'),
        ('Wealth', 'Wealth'),
        ('War', 'War'),
        ('Golden', 'Golden'),
        ('Calamity', 'Calamity'),
        ('Restoration', 'Restoration'),
        ('Industry', 'Industry'),
        ('Modern', 'Modern'),
        ('Technology', 'Technology')
    ])

