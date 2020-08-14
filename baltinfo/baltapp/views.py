from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .sqlighter import get_data_for_app, insert_data_in_db, Q_1, Q_2, Q_3

from .forms import ChannelForm
from .utils import convert


def set_channels(request):
    if request.method == "POST":
        channel_form = ChannelForm(request.POST)
        if channel_form.is_valid():
            channels = request.POST.get("ch").split()  # list
            channels_records = convert(channels)  # list of tuples
            insert_data_in_db(data=channels_records)
            url = request.build_absolute_uri('/userschannels/')
            # print(request.build_absolute_uri('/userschannels/'))
            return HttpResponseRedirect(url)
        else:  # невалидные данные
            return HttpResponse("Данные не корректны!")
    else:  # начало работы с приложением
        channel_form = ChannelForm()
        for_context = {"form": channel_form}
        return render(request, "first_page.html", for_context)


def userschannels(request):
    if request.method == "POST":
        # Получаем выбранные пользователем каналы
        channels = request.POST.getlist("chnls")  # list
        if not channels:  # пользователь приложения не выбрал Telegram-каналы
            return HttpResponse("Выберите хотя бы один канал!")
        channels = ", ".join('"' + ch + '"' for ch in channels)  # str
        data = get_data_for_app(query=Q_2, clause=channels)
        for_context = {"telegram": data}
        return render(request, "about_userchannel.html", for_context)
    else:  # получение списка Telegram-каналов
        data = get_data_for_app(query=Q_1, clause=None)
        if not data:  # таблицы БД пусты
            return HttpResponse("Создайте каналы и привлеките подписчиков!")
        for_context = {"telegram": data}
        return render(request, "index.html", for_context)
