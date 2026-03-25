# test.py
# Модуль для автоматического тестирования функций из main.py
# Используем встроенный в Python unittest.

import unittest
# Импортируем все тестируемые функции из основного файла
from main import add, subtract, multiply, divide, mod


# ===================== Тесты для арифметических операций =====================
class TestMath(unittest.TestCase):
    """Класс, содержащий тесты для базовых арифметических операций."""

    def test_add(self):
        """Проверяем функцию сложения (add)."""
        # Проверяем, что результат сложения двух чисел соответствует ожидаемому.
        # assertEqual сравнивает первый аргумент (результат) со вторым (ожидание).
        self.assertEqual(add(2, 5), 7)   # 2+5 = 7 – правильный результат
        # Здесь специально указываем неверное ожидание, чтобы показать, как тест падает.
        # При нормальной работе мы пишем только правильные ожидания.
        # Но для демонстрации оставляем один ошибочный тест – он упадёт.
        self.assertEqual(add(3, 7), 9)   # 3+7 = 10, а не 9 – ошибка

    def test_subtract(self):
        """Проверяем функцию вычитания (subtract)."""
        self.assertEqual(subtract(7, 4), 3)   # 7-4 = 3 – верно
        self.assertEqual(subtract(4, 2), 1)   # 4-2 = 2, а не 1 – ошибка

    def test_multiply(self):
        """Проверяем функцию умножения (multiply)."""
        self.assertEqual(multiply(2, 5), 12)  # 2*5 = 10, а не 12 – ошибка
        self.assertEqual(multiply(3, 6), 18)  # 3*6 = 18 – верно

    def test_divide(self):
        """Проверяем функцию деления (divide)."""
        self.assertEqual(divide(4, 2), 3)    # 4/2 = 2, а не 3 – ошибка
        self.assertEqual(divide(20, 5), 4)   # 20/5 = 4 – верно


# ===================== Тесты с использованием assertNotEqual =====================
class TestMathNotEqual(unittest.TestCase):
    """Класс, демонстрирующий assertNotEqual – проверку на неравенство."""

    def test_add_not_equal(self):
        """Для сложения проверяем, что неверный результат действительно не равен."""
        # assertNotEqual проверяет, что два значения НЕ равны.
        self.assertNotEqual(add(3, 7), 9)   # 3+7 = 10, а 10 ≠ 9 – тест пройден

    def test_subtract_not_equal(self):
        """Для вычитания проверяем неверный результат."""
        self.assertNotEqual(subtract(4, 2), 1)   # 4-2 = 2, 2 ≠ 1 – тест пройден

    def test_multiply_not_equal(self):
        """Для умножения проверяем неверный результат."""
        self.assertNotEqual(multiply(2, 5), 12)  # 10 ≠ 12 – тест пройден

    def test_divide_not_equal(self):
        """Для деления проверяем неверный результат."""
        self.assertNotEqual(divide(4, 2), 3)     # 2 ≠ 3 – тест пройден


# ===================== Тесты для функции проверки чётности =====================
def check(number):
    """Вспомогательная функция для тестирования assertTrue/assertFalse.
    Возвращает True, если число чётное, иначе False."""
    return number % 2 == 0

class TestCheck(unittest.TestCase):
    """Класс для демонстрации assertTrue и assertFalse."""

    def test_even_numbers(self):
        """Проверяем, что чётные числа дают True."""
        self.assertTrue(check(2))      # 2 – чётное → True
        self.assertTrue(check(6))      # 6 – чётное → True
        self.assertTrue(check(220))    # 220 – чётное → True

    def test_odd_numbers_with_not(self):
        """Проверяем, что нечётные числа с not дают True."""
        # Для нечётных чисел check() вернёт False. Добавляем not, чтобы получить True.
        self.assertTrue(not check(1))   # not False = True
        self.assertTrue(not check(3))   # not False = True
        self.assertTrue(not check(57))  # not False = True

    def test_odd_numbers_assertFalse(self):
        """Используем assertFalse напрямую для нечётных чисел."""
        self.assertFalse(check(1))      # 1 – нечётное → False
        self.assertFalse(check(3))      # 3 – нечётное → False
        self.assertFalse(check(57))     # 57 – нечётное → False


# ===================== Тесты для деления с обработкой ошибок =====================
class TestDivideExceptions(unittest.TestCase):
    """Проверяем, что при делении на ноль функция divide выбрасывает исключение."""

    def test_divide_success(self):
        """Проверяем корректное деление без ошибок."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        """Проверяем, что при попытке деления на ноль возникает исключение ValueError."""
        # assertRaises(исключение, функция, аргументы) – проверяет, что функция
        # выбросит указанное исключение при вызове с данными аргументами.
        self.assertRaises(ValueError, divide, 6, 0)


# ===================== Тесты для новой функции mod (остаток от деления) =====================
class TestMod(unittest.TestCase):
    """Класс для тестирования функции mod (остаток от деления)."""

    def test_mod_success(self):
        """Проверяем корректные вычисления остатка."""
        # Остаток от деления 10 на 3 = 1
        self.assertEqual(mod(10, 3), 1)
        # Остаток от деления 8 на 4 = 0
        self.assertEqual(mod(8, 4), 0)
        # Остаток от деления 7 на 2 = 1
        self.assertEqual(mod(7, 2), 1)
        # Дополнительная проверка: 15 % 6 = 3
        self.assertEqual(mod(15, 6), 3)

    def test_mod_by_zero(self):
        """Проверяем, что при попытке деления на ноль возникает исключение ValueError."""
        # При вызове mod(6, 0) должно возникнуть ValueError
        self.assertRaises(ValueError, mod, 6, 0)


# ===================== Запуск всех тестов =====================
if __name__ == '__main__':
    # unittest.main() автоматически находит все классы, унаследованные от TestCase,
    # и запускает все методы, имена которых начинаются с test_.
    unittest.main()