from unittest import TestCase, main
from Test_task_1 import get_score, generate_game


class TestGetScore(TestCase):
    def setUp(self):
        self.game_stamps = generate_game()

    def test_get_score_when_offset_exists(self):
        offset = self.game_stamps[0]['offset']  # берем первое значение offset
        score = get_score(self.game_stamps, offset)
        self.assertIsNotNone(score)
        self.assertNotEqual(score, 'no data')

    def test_get_score_middle_offset(self):
        middle_offset = len(self.game_stamps) // 2
        offset = self.game_stamps[middle_offset]['offset']  # берем среднее значение offset
        score = get_score(self.game_stamps, offset)
        self.assertIsNotNone(score)
        self.assertNotEqual(score, 'no data')

    def test_get_score_when_offset_is_last(self):
        offset = self.game_stamps[-1]['offset']      # последний offset
        score = get_score(self.game_stamps, offset)
        self.assertIsNotNone(score)
        self.assertNotEqual(score, 'no data')

    def test_get_score_when_offset_is_zero(self):
        offset = 0                                    # когда ноль
        score = get_score(self.game_stamps, offset)
        self.assertIsNotNone(score)
        self.assertNotEqual(score, 'no data')

    def test_get_score_when_offset_not_exists(self):
        offset = 999999                               # используем несуществующий offset
        score = get_score(self.game_stamps, offset)
        self.assertEqual(score, 'no data')

    def test_get_score_when_offset_is_negative(self):
        offset = -1                                   # отрицательные значения
        score = get_score(self.game_stamps, offset)
        self.assertEqual(score, 'no data')


if __name__ == '__main__':
    main()
