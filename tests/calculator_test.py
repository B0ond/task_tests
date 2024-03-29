from unittest import TestCase, main
from temp_2 import calc


class TestCalculator(TestCase):
    def test_plus(self):
        self.assertEqual(calc('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calc('3-2'), 1)

    def test_division(self):
        self.assertEqual(calc('54/2'), 27)

    def test_multiple(self):
        self.assertEqual(calc('25*4'), 100)

    # далее тесты где может пойти что-то не так
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('djhfjghkdjfh')
        self.assertEqual('Выражение должно содержать хотя бы 1 знак из: +-/*', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('2+2+3')
        self.assertEqual('Выражение должн осодержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('2+2*5')
        self.assertEqual('Выражение должн осодержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calc('2+2*5/3.4')
        self.assertEqual('Выражение должн осодержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('a+b')
        self.assertEqual('Выражение должн осодержать 2 целых числа и 1 знак', e.exception.args[0])
    
    def test_many_signs_together(self):
        with self.assertRaises(ValueError) as e:
            calc('2+++5')
        self.assertEqual('Выражение должн осодержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_two_different_signs_together(self):
        with self.assertRaises(ValueError) as e:
            calc('2++*+5')
        self.assertEqual('Выражение должн осодержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()
