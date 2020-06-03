from django.db import models
from django.core import validators


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='категория')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-name']

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='город')
    source = models.URLField(max_length=1000, verbose_name='ссылка на ресурс', blank=True, null=True)


    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
        ordering = ['name']

    def __str__(self):
        return self.name


class News(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', blank=True, default='', related_name='entries',
                                 on_delete=models.CASCADE)
    icon = models.CharField(max_length=1000, verbose_name='ссылка на картинку', blank=True, null=True)
    description = models.TextField(editable=False, verbose_name='Текст новости', blank=True, null=True)
    url_source = models.URLField(max_length=1000, verbose_name='ссылка на ресурс', blank=True, null=True)
    media = models.URLField(max_length=1000, verbose_name='Ссылка на медиа', blank=True, null=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering  = ['-published']

    def __str__(self):
        return self.title


class Messages(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя отправителя', null=False, blank=False, validators=[validators.MaxLengthValidator(20,message='Введите Ваше имя')])
    email = models.EmailField(max_length=100, verbose_name='Электронная почта', null=False, blank=False, validators=[validators.EmailValidator(message='Введите коректный адрес электронной почты')])
    text = models.TextField(max_length=500, verbose_name='Текст сообщения', null=False, blank=False, validators=[validators.MaxLengthValidator(500, message='Допустимое количество символов привысило 500'), validators.MinLengthValidator(0, message='Введите сообщение')])
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['-published']


class CityNews(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок', blank=True)
    city = models.ForeignKey(City, verbose_name='Город', blank=True, default='', related_name='cities',
                                 on_delete=models.CASCADE)
    icon = models.CharField(max_length=1000, verbose_name='ссылка на картинку', blank=True, null=True)
    description = models.TextField(editable=False, verbose_name='Текст новости', blank=True, null=True)
    url_source = models.URLField(max_length=1000, verbose_name='ссылка на ресурс', blank=True, null=True)
    media = models.URLField(max_length=1000, verbose_name='Ссылка на медиа', blank=True, null=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости регионов'
        ordering  = ['-published']

    def __str__(self):
        return self.title


class Weather(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, verbose_name='Город', blank=True, default='', related_name='weather_cities',
                                 on_delete=models.CASCADE)
    day = models.IntegerField(verbose_name='день')
    month = models.CharField(max_length=20, verbose_name='месяц')
    year = models.IntegerField(verbose_name='год')
    hour = models.IntegerField(verbose_name='час')
    weekday = models.CharField(max_length=200, verbose_name='день недели')
    cloudiness = models.CharField(max_length=30, verbose_name='облачность')
    precipitation = models.CharField(max_length=30, verbose_name='осадки')
    pressure_min = models.CharField(max_length=30, verbose_name='минимальное давление')
    pressure_max = models.CharField(max_length=30, verbose_name='максимальное давление')
    wind_min = models.CharField(max_length=30, verbose_name='мин скорость ветра')
    wind_max = models.CharField(max_length=30, verbose_name='макс скорость ветра')
    wind_direction = models.CharField(max_length=30, verbose_name='направление ветра')
    humidity_min = models.CharField(max_length=30, verbose_name='мин влажность')
    humidity_max = models.CharField(max_length=30, verbose_name='макс влажность')
    heat_min = models.CharField(max_length=30, verbose_name='мин температура ощущаемая')
    heat_max = models.CharField(max_length=30, verbose_name='макс температура ощущаемая')
    temperature_min = models.CharField(max_length=30, verbose_name='минимальная температура')
    temperature_max = models.CharField(max_length=30, verbose_name='максимальная температура')

    class Meta:
        verbose_name = 'погода'
        ordering  = ['-published']