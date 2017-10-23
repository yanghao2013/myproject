from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

def logger_test(request):
    fomat = '%(clientip)s %(user)s %(message)s' % {'clientip':'192.168.1.1','user':'yanghao','message':'log some'}
    logger.info(fomat)
    logger.error('Something went wrong!')
    try:
        a = 5/0
    except Exception as e:
        logger.error(e)

    return HttpResponse("hi Hello World!")
