from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def my_view(request):
    user = request.user
    items = ['Item 1', 'Item 2', 'Item 3']
    page_title = "My Custom Page Title"
    is_changed = True  # You would set this based on some condition
    
    context = {
        'user': user,
        'items': items,
        'page_title': page_title,
        'is_changed': is_changed,  # Include the is_changed flag in the context
    }
    
    return render(request, 'template.html', context)
