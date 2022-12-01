from django.shortcuts import render, HttpResponse
from .pdf import render_to_pdf
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, "home.html")

@csrf_exempt
@require_http_methods(["POST"])
def pdf(request):
    pdf=render_to_pdf("pdf.html", json.loads(request.body))
    return HttpResponse(pdf, content_type="application/pdf")

@csrf_exempt
@require_http_methods(["POST"])
def order(request):
    pdf=render_to_pdf("order.html", json.loads(request.body))
    return HttpResponse(pdf, content_type="application/pdf")


 