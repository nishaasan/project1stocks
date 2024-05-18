from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Watchlist, Stock
from .forms import WatchlistForm, StockForm
from django.conf import settings
import requests

@login_required
def dashboard(request):
    watchlists = Watchlist.objects.filter(user=request.user)
    stock_data = {}

    # Debug print to check if ALPHA_VANTAGE_API_KEY is available
    print("ALPHAVANTAGE_API_KEY ", getattr(settings, 'ALPHAVANTAGE_API_KEY ', 'Not Found'))

    for watchlist in watchlists:
        for stock in watchlist.stock_set.all():
            response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock.symbol}&interval=1min&apikey={settings.ALPHA_VANTAGE_API_KEY}')
            data = response.json()
            if 'Time Series (1min)' in data:
                stock_data[stock.symbol] = list(data['Time Series (1min)'].items())[0]  # Get the most recent data point
            else:
                stock_data[stock.symbol] = {}

    return render(request, 'stocks1/dashboard.html', {'watchlists': watchlists, 'stock_data': stock_data})

@login_required
def add_watchlist(request):
    if request.method == 'POST':
        form = WatchlistForm(request.POST)
        if form.is_valid():
            watchlist = form.save(commit=False)
            watchlist.user = request.user
            watchlist.save()
            return redirect('dashboard')
    else:
        form = WatchlistForm()
    return render(request, 'stocks1/watchlist.html', {'form': form})

@login_required
def add_stock(request, watchlist_id):
    watchlist = Watchlist.objects.get(id=watchlist_id)
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.watchlist = watchlist
            stock.save()
            return redirect('dashboard')
    else:
        form = StockForm()
    return render(request, 'stocks1/addstock.html', {'form': form})
