from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from .models import Presentation, Slide


def home(request, presentation_id=None):
    if not presentation_id:
        try:
            presentation_id = Presentation.objects.all()[0].pk
        except IndexError:
            return HttpResponse()

    slides = Slide.objects.filter(presentation=presentation_id).order_by('index')
    return render_to_response('presentation.html', {"slides": slides}, context_instance=RequestContext(request))
