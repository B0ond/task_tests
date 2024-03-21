INITIAL_STAMP = [{"offset": 0}, {"offset": 1}, {"offset": 2},
                 {"offset": 3}, {"offset": 4}, {"offset": 5},
                 {"offset": 6}, {"offset": 7}, {"offset": 8},
                 {"offset": 9}, {"offset": 10}, {"offset": 11}]


def get_score(game_stamps, offset):
    left, right = 0, len(game_stamps) - 1

    # Бинарный поиск для нахождения индекса первой метки с временем, большим или равным указанному времени
    while left <= right:
        mid = (left + right) // 2
        if game_stamps[mid]["offset"] >= offset:
            right = mid - 1
        else:
            left = mid + 1
    if left == len(game_stamps) or game_stamps[left]["offset"] != offset:
        return "no data"
    else:
        return game_stamps[left]["offset"]




print(get_score(INITIAL_STAMP, 7))


# def get_score(game_stamps, offset):
#     left, right = 0, len(game_stamps) - 1
#
#     # Бинарный поиск для нахождения индекса первой метки с временем, большим или равным указанному времени
#     while left <= right:
#         mid = (left + right) // 2
#         if game_stamps[mid]["offset"] >= offset:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     # Если нет метки с указанным временем, вернуть счет ближайшей предыдущей метки
#     if left == len(game_stamps) or game_stamps[left]["offset"] != offset:
#         return 'no data'
#     else:
#         return game_stamps[left]["score"]["away"], game_stamps[left]["score"]["home"]
