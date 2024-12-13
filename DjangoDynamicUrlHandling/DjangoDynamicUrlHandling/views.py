from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

ALLOWED_REGIONS = {'us', 'uk', 'in'}
CONTENT = {'us':'US', 'uk':'UK', 'in':'India'}

def home_view(request, region=None):
    print("Home View - Region Stored in Session : ",request.session['region'])
    if region not in ALLOWED_REGIONS: #return 400 response if region is not allowed
        return HttpResponseBadRequest("<h1>400 Bad Request</h1><p>Invalid region.</p>")
    
    request.session['region'] = region #store region code in session for future use
    return render(request, 'home.html', {'region_name': CONTENT[str(region)]})

def about_view(request, region=None):
    print("About View - Region Stored in Session : ",request.session['region'])
    if region not in ALLOWED_REGIONS: #return 400 response if region is not allowed
        return HttpResponseBadRequest("<h1>400 Bad Request</h1><p>Invalid region.</p>")

    request.session['region'] = region #store region code in session for future use
    return render(request, 'about.html', {'region_name': CONTENT[str(region)]})

