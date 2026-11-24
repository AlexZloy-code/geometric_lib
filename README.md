# Документация проекта Geometric Lib

## Общее описание
Проект Geometric Lib - это библиотека на Python для вычисления площади и периметра геометрических фигур: круга, прямоугольника, квадрата и треугольника.

## Модули и формулы
| Модуль        | Описание конкретного модуля          | Формула площади | Формула периметра |
| ------------- |:------------------------------------:|:---------------:|:-----------------:|
| `circle.py`   | [circle.md](./docs/circle.md)        | S = πR²         | P = 2πR           |
| `rectangle.py`| [rectangle.md](./docs/rectangle.md)  | S = ab          | P = 2a + 2b       |
| `square.py`   | [square.md](./docs/square.md)        | S = a²          | P = 4a            |
| `triangle.py` | [triangle.md](./docs/triangle.md)    | S = a * h / 2   | P = a + b + c     |

## Информация о тестах
<!-- Подготовка к CI -->
[О тестовой системе](./docs/tests.md)

|Модуль         |Результаты тестов| 
| ------------- |:---------------:|
|All tests      | 39/42           |
|test_circle    | 12/12           |
|test_rectangle | 8/10            |
|test_square    | 9/10            |
|test_triangle  | 10/10           |

## Коммиты
* `94bc231` - add .gitignore
* `b84df02` - docs: Change path to README and change info about tests
* `9287515` - Add tests files and test_runner file
* `62695c0` - docs: update README.md
* `d534780` - docs: add modules-info files
* `bca8a10` - docs: add comments in all functions
* `8ee295c` - docs: add description for triangle-module
* `305b40c` - feat: add new moduls (rectangle.py, triangle.py)
* `d078c8d` - L-03: Docs added
* `8ba9aeb` - L-03: Circle and square added
