from django.db import connection

# Запрос для получения каналов из БД
Q_1 = """
    SELECT ch_id AS chnl, username
    FROM channel
    """

# Запрос для получения подписчиков, которые состоят как минимум в 2-ух каналах,
# предварительно выбранных пользователем django-приложения
Q_2 = """
    SELECT full_name AS user, GROUP_CONCAT(username_ch, ", ") AS channels
    FROM ch_subscr JOIN (
        SELECT subscr_id, COUNT(subscr_id) AS Встречаемость_подписчика
        FROM ch_subscr
        WHERE ch_id IN ( {0} )
        GROUP BY subscr_id
        HAVING COUNT(subscr_id) > 1) as f_table
    USING(subscr_id)
    WHERE ch_id IN ( {0} )
    GROUP BY subscr_id
    """

# Запрос для вставки названий каналов в БД
Q_3 = """
    INSERT INTO channel (ch_id, username, title)
    VALUES (%s, %s, %s)
    """


def get_data_for_app(
    query=Q_2,
    clause=None
):

    """
    Получает информацию из БД в зависимости от запроса и условия
    :param clause: условие для выбора по горизонтали - непустая строка или
                    falsy-значение
    :return: list of dicts
    """

    with connection.cursor() as cursor:
        if clause:  # выбираем подписчиков, состоящих в 2-ух каналах (min)
            query = query.format(clause)
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        records = cursor.fetchall()
        return [
            dict(zip(columns, row))
            for row in records
        ]


def insert_data_in_db(
    query=Q_3,
    data=("-1001434239048", "@abba", "proba")
):

    """
    Вставляет информацию о Telegram-каналах в БД
    :param data: имена каналов как часть параметров INSERT-запроса - список кортежей

    """

    with connection.cursor() as cursor:
        cursor.executemany(query, data)
