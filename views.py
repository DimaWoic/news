from django.shortcuts import render, get_object_or_404
from .models import News, Category, Messages, City, CityNews
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import MessageForm
from django.core.mail import EmailMessage
import datetime
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from django.views.generic.list import ListView


def index(request):
    news = News.objects.filter(published__date__gte=datetime.datetime.today().date())
    categories = Category.objects.all()
    regionsnews = CityNews.objects.filter(published__date__gte=datetime.datetime.today().date())
    cities = City.objects.all()
    list_arrays = [[], [], [], [], [], [], []]
    list_city = []
    for c in cities:
        list_city.append(c.name)

    for array in list_arrays:
        for city in list_city:
            if city not in array:
                if len(array) <= 14:
                    array.append(city)
                    list_city.pop(list_city.index(city))

    context = {'news': news, 'categories': categories, 'regionsnews': regionsnews, 'city': cities}
    return render(request, 'news/index.html', context)


def by_category(request, category_id):
    news = News.objects.filter(category=category_id).filter(published__date__gte=datetime.datetime.today().date())
    regionsnews = CityNews.objects.filter(published__date__gte=datetime.datetime.today().date())
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'news': news, 'categories': categories, 'current_category': current_category, 'regionsnews': regionsnews}
    return render(request, 'news/by_category.html', context)


def feedback(request):
    if request.method == 'POST':
       feed = MessageForm(request.POST)
       if feed.is_valid():
           feed.save()
           email = EmailMessage(subject='У Вас новое сообщение в форме обратной связи на сайта новостей Magpie',
                                 body=str(Messages.objects.first().text), to=['wdv85@mail.ru'])
           return render(request, 'news/msgsend.html')
       else:
          context = {'form': feed}
          return render(request, 'news/feedback.html', context)
    else:
        feed = MessageForm()
        context = {'form': feed}
        return render(request, 'news/feedback.html', context)


@api_view(['GET'])
def api_news(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class RobotsTxt(TemplateView):
    template_name = 'news/robots.txt'
    content_type = "text/plane"


def by_regions(request, city_id):
    region = CityNews.objects.filter(city=city_id).filter(published__date__gte=datetime.datetime.today().date())
    allnews= News.objects.filter(published__date__gte=datetime.datetime.today().date())
    categories = Category.objects.all()
    city = City.objects.all()
    city_list = []
    current_city = City.objects.get(pk=city_id)
    context = {'regionnews': region, 'worldnews': allnews, 'categories': categories, 'city': city,
               'current_city': current_city}
    return render(request, 'news/by_region.html', context)


def by_region_category(request, city_id, category_id):
    region = CityNews.objects.filter(city=city_id).filter(published__date__gte=datetime.datetime.today().date())
    news = News.objects.filter(category=category_id).filter(published__date__gte=datetime.datetime.today().date())
    categories = Category.objects.all()
    city = City.objects.all()
    current_city = City.objects.get(pk=city_id)
    context = {'regionnews': region, 'worldnews': news, 'categories': categories, 'city': city,
               'current_city': current_city}
    return render(request, 'news/byregandcateg.html', context)


class ByRegionCategory(ListView):
    context_object_name = 'region'
    template_name = 'news/byregandcateg.html'

    def get_queryset(self):
        return CityNews.objects.filter(city=self.kwargs['city_id']).filter\
            (published__date__gte=datetime.datetime.today().date())

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['news'] = News.objects.filter(category=self.kwargs['category_id'])\
            .filter(published__date__gte=datetime.datetime.today().date())
        context['category'] = Category.objects.all()
        context['current_city'] = City.objects.get(pk=self.kwargs['city_id'])
        context['city'] = City.objects.all()
        return context