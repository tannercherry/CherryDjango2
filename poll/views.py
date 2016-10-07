from django.shortcuts import render
from django.http import HttpResponse

import time
# Create you views here.
def main(request):
    return HttpResponse("Current date and time: " + time.strftime("%c"));