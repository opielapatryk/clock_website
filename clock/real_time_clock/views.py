# from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(req):
    current_date = datetime.datetime.now()
    html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_date
    return HttpResponse(html)
# Create your views here.
# def hello_world(req):
#     return render(req, "real_time_clock.html", {})