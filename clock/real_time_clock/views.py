from django.shortcuts import render

# Create your views here.
def hello_world(req):
    return render(req, "real_time_clock.html", {})