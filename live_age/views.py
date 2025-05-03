from django.http import JsonResponse
from django.shortcuts import render
import redis
import json
from datetime import datetime

# Connect to Redis Cloud
r = redis.Redis(
    host='redis-11534.crce179.ap-south-1-1.ec2.redns.redis-cloud.com',
    port=11534,
    password='e2F5DI7U30lhAMFpk8SWo519Z8Wk5hXR',
    decode_responses=True
)

def live_age_view(request):
    return render(request, 'live_age/display.html')

def get_live_age(request):
    data = r.lindex('raw_queue', 0)
    if not data:
        return JsonResponse({'error': 'No data found'})

    data = json.loads(data)
    name = data['name']
    dob = datetime.strptime(data['dob'], '%Y-%m-%d')
    now = datetime.now()
    delta = now - dob

    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    age_str = f"{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    return JsonResponse({'name': name, 'age': age_str})
