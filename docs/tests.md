# Документация по тестированию проекта

Для проверки корректности работы геометрических функций (`area` и `perimeter`) для круга, прямоугольника, квадрата и треугольника создан набор тестов с использованием стандартной библиотеки Python `unittest`.

## Структура тестов

Все тестовые файлы расположены в директории `tests/` и соответствуют модулям в корне проекта:

* `tests/test_circle.py` — тесты для модуля `circle.py` (площадь и длина окружности).
* `tests/test_rectangle.py` — тесты для модуля `rectangle.py` (площадь и периметр прямоугольника).
* `tests/test_square.py` — тесты для модуля `square.py` (площадь и периметр квадрата).
* `tests/test_triangle.py` — тесты для модуля `triangle.py` (площадь по основанию и высоте, периметр по трём сторонам).
* `tests/tests_runner.py` (или `run_tests.py`) — кастомный скрипт для запуска всех тестов и вывода сводной статистики.

## Что проверяют тесты

Каждый тестовый модуль разделён на несколько логических групп (`TestCase`):

1. **Позитивные тесты (`PositiveTestCase`)**
   * Проверка вычислений на нулевых значениях (`0`).
   * Проверка на положительных целых числах (`int`).
   * Проверка на числах с плавающей точкой (`float`) с учётом допустимой погрешности через `assertAlmostEqual`.
2. **Негативные тесты (`NegativeTestCase`)**
   * **Проверка типов данных:** передача некорректных типов (`str`, `None`, `list`, `dict`), ожидается выброс исключения `TypeError`.
   * **Проверка количества аргументов:** вызов функций без аргументов, с недостающим или избыточным количеством параметров, ожидается `TypeError`.
   * **Проверка на предельную точность** намеренно непроходимые тесты с использованием модуля `decimal.Decimal`.

---

## Как запускать тесты

Все команды выполняются из **корневой директории проекта**.

### 1. Запуск через сводный скрипт (`run_tests.py` / `tests_runner.py`)

Скрипт запускает все тестовые файлы по очереди и выводит краткий отчёт в формате `имя_модуля - пройдено/всего`:

```bash
python3 tests_runner.py
```

**Пример вывода:**
```text
test_circle - 12/12



test_rectangle - 8/10
test_area_invalid_type (test_rectangle.RectangleAreaNegativeTestCase.test_area_invalid_type)
Traceback (most recent call last):
  File "/home/sasha/ITMO/ISPRO/lab_4/geometric_lib/tests/test_rectangle.py", line 39, in test_area_invalid_type
    with self.assertRaises(TypeError):  # wrong
AssertionError: TypeError not raised

test_perimeter_invalid_type (test_rectangle.RectanglePerimeterNegativeTestCase.test_perimeter_invalid_type)
Traceback (most recent call last):
  File "/home/sasha/ITMO/ISPRO/lab_4/geometric_lib/tests/test_rectangle.py", line 59, in test_perimeter_invalid_type
    with self.assertRaises(TypeError): # wrong
AssertionError: TypeError not raised




test_square - 9/10
test_perimeter_invalid_type (test_square.SquarePerimeterNegativeTestCase.test_perimeter_invalid_type)
Traceback (most recent call last):
  File "/home/sasha/ITMO/ISPRO/lab_4/geometric_lib/tests/test_square.py", line 55, in test_perimeter_invalid_type
    with self.assertRaises(TypeError): #wrong
AssertionError: TypeError not raised




test_triangle - 10/10



All tests - 39/42
```

### 2. Стандартный запуск всех тестов через `unittest`

Для запуска всех тестов с подробным логом выполнения каждого метода (`-v`):

```bash
python3 -m unittest discover -v -s tests
```

### 3. Запуск отдельного тестового файла

Чтобы проверить только одну фигуру (например, круг), укажите путь к файлу или имя модуля через точку:

```bash
python3 -m unittest -v tests/test_circle.py
python3 -m unittest -v tests/test_rectangle.py
python3 -m unittest -v tests/test_square.py
python3 -m unittest -v tests/test_triangle.py
```
или
```bash
python3 -m unittest -v tests.test_circle
python3 -m unittest -v tests.test_rectangle
python3 -m unittest -v tests.test_square
python3 -m unittest -v tests.test_triangle
```
