from django import forms
from .models import *

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['name']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['symbol']
