from django.shortcuts import render, HttpResponse
from .pdf import render_to_pdf
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["POST"])
def templateRed(request):
    pdf=render_to_pdf("templateRed.html", json.loads(request.body))
    return HttpResponse(pdf, content_type="application/pdf")

