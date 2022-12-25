from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
import pdfkit

def render_to_pdf(template_src, context_dict={}, name=""):
	template = get_template(template_src)
	html  = template.render(context_dict)
	f = open('temp.html', 'w')
	options = {
          'page-size': 'Letter',
          'encoding': "UTF-8",
       }
	pdf = pdfkit.from_string(html, options=options)
	response = HttpResponse(pdf,content_type='application/pdf')
	return response