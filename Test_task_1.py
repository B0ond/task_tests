from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001  # вероятность что изменится

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):  # previous_value вставляется в return
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED  # True or False
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    # если score_changed True и с вероятностью 45% home_score_change будет равнятся 1
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()


def get_score(game_stamps, offset):
    left, right = 0, len(game_stamps) - 1

    # Бинарный поиск для нахождения индекса первой метки с временем, большим или равным указанному времени
    while left <= right:
        mid = (left + right) // 2
        if game_stamps[mid]["offset"] >= offset:
            right = mid - 1
        else:
            left = mid + 1

    # Если нет метки с указанным временем, вернуть счет ближайшей предыдущей метки
    if left == len(game_stamps) or game_stamps[left]["offset"] != offset:
        return game_stamps[left - 1]["score"]["home"], game_stamps[left - 1]["score"]["away"], 'else'
    else:
        return game_stamps[left]["score"]["home"], game_stamps[left]["score"]["away"], len(game_stamps) - 1


pprint(get_score(game_stamps, 50000))
# pprint(game_stamps)







# def get_score(game_stamps, offset):
#     '''
#         Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
#         Please pay attention to that for some offsets the game_stamps list may not contain scores.
#     '''
#     # return home, away


