from django.http import HttpResponse
from django.shortcuts import render

from .sqlighter import get_data_for_app, Q_1, Q_2


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
    else:  # начало работы с приложением - получение списка Telegram-каналов
        data = get_data_for_app(query=Q_1, clause=None)
        if not data:  # таблицы БД пусты
            return HttpResponse("Создайте каналы и привлеките подписчиков!")
        for_context = {"telegram": data}
        return render(request, "index.html", for_context)
