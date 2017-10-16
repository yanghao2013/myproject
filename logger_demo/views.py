from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

def logger_test(request):
    logging.info("log something")
    logger.error('Something went wrong!')
    return HttpResponse("hi Hello World!")
