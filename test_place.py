INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def calculate_score(previous_value):
    offset_change = 2
    home_score_change = 3
    away_score_change = 4
    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    current_stamp = INITIAL_STAMP
    out = calculate_score(current_stamp)
    return out


print(generate_game())