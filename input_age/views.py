from django.shortcuts import render, redirect
from .forms import AgeInputForm
import redis
import json
from django.urls import resolve, Resolver404

# Connect to Redis Cloud
r = redis.Redis(
    host='redis-11534.crce179.ap-south-1-1.ec2.redns.redis-cloud.com',
    port=11534,
    password='e2F5DI7U30lhAMFpk8SWo519Z8Wk5hXR',
    decode_responses=True
)

def input_view(request):
    if request.method == 'POST':
        form = AgeInputForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'dob': str(form.cleaned_data['dob'])  # Convert datetime to string
            }
            r.lpush('raw_queue', json.dumps(data))  # Push to Redis queue
        
        # If /live-age/ route doesn't exist, render fallback template
        print('input_age fallback triggered')
        data = r.lindex('raw_queue', 0)
        data = json.loads(data)
        return render(request, 'input_age/display.html', {'data': data})
    else:
        form = AgeInputForm()

    return render(request, 'input_age/form.html', {'form': form})
