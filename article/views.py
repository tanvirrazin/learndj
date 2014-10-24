from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView

from article.models import Article

# Create your views here.


def hello(request):
	name = 'Razin'
	html = "<html><body></body>Hi %s, This seems to have worked!</html>" % name
	return HttpResponse(html)

def hello_template(request):
	name = 'Razin'
	t = get_template('hello.html')
	html = t.render(Context({ 'name': name}))
	return HttpResponse(html)

def hello_template_simple(request):
	name = 'Razin'
	return render_to_response('hello.html', { 'name': name })


class HelloTemplate(TemplateView):

	template_name = 'hello_class.html'

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'Razin'
		return context


def articles(request):
	context_obj = {
		'articles': Article.objects.all()
	}
	return render_to_response('articles.html', context_obj)

def article(request, article_id=1):
	context_obj = {
		'article': Article.objects.get(id=article_id)
	}
	return render_to_response('article.html', context_obj)