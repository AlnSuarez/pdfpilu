from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
import pdfkit

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	f = open('temp.html', 'w')
	options = {
          'page-size': 'A6',
          'encoding': "UTF-8",
       }
	filename =  "template_puebla.pdf"
	pdf = pdfkit.from_string(html, False, options=options)
	response = HttpResponse(pdf,content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
	return response