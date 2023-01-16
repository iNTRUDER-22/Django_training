from django.shortcuts import render
from django.http import HttpResponse

def advertisement_list(request, *args, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    advertisement = ["Мастер на час", "Мои вызовы", "Мой профиль"]
    return render(request, 'advertisement/advertisement_list.html', {'ip_address':ip, 'advertisements':advertisement})

def advertisement1(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement1.html', {})

def contacts(request, *args, **kwargs):
    contacts = ["99 999 99 99", "11 111 11 11", "22 222 22 22", "33 333 33 33"]
    return render(request, 'advertisement/contacts.html', {'contacts_list':contacts})

def about(request, *args, **kwargs):
    about_h4 = 'Название компании'
    about_text = ['Раздел «О нас» дает посетителям сайта представление о компании или личности. Цифры, кейсы, ссылки на крупных заказчиков — подтвержденная информация повышает ваш авторитет и формирует доверие со стороны аудитории. Здесь вы показываете свою значимость и объясняете, почему выгодно быть вашим клиентом.','Этот раздел подходит для краткого рассказа о команде и истории развития компании. Покажите лица, которые стоят за продуктом — открытость расположит к вам людей. Раскройте свою миссию. Например, вы не просто торгуете техникой, а имеете цель — облегчить быт и улучшить качество жизни. Если есть награды и сертификаты, разместите их здесь.']
    return render(request, 'advertisement/about.html', {'about_h4': about_h4, 'about_text': about_text})

def categories(request, *args, **kwargs):
    categories = ["Категория 1", "Категория 2", "Категория 3", "Категория 4"]
    return render(request, 'advertisement/categories.html', {'categories':categories})

def regions(request, *args, **kwargs):
    regions = ["Регион 1", "Регион 2", "Регион 3", "Регион 4"]
    return render(request, 'advertisement/regions.html', {'regions':regions})