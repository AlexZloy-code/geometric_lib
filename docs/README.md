# Документация проекта Geometric Lib

## Общее описание
Проект Geometric Lib - это библиотека на Python для вычисления площади и периметра геометрических фигур: круга, прямоугольника, квадрата и треугольника.

## Модули и формулы
| Модуль        | Описание конкретного модуля          | Формула площади | Формула периметра |
| ------------- |:------------------------------------:|:---------------:|:-----------------:|
| `circle.py`   | [circle.md](../docs/circle.md)       | S = πR²         | P = 2πR           |
| `rectangle.py`| [rectangle.md](../docs/rectangle.md) | S = ab          | P = 2a + 2b       |
| `square.py`   | [square.md](../docs/square.md)       | S = a²          | P = 4a            |
| `triangle.py` | [triangle.md](../docs/triangle.md)   | S = a * h / 2   | P = a + b + c     |

## Коммиты
* `62695c0` - docs: update README.md
* `d534780` - docs: add modules-info files
* `bca8a10` - docs: add comments in all functions
* `8ee295c` - docs: add description for triangle-module
* `305b40c` - feat: add new moduls (rectangle.py, triangle.py)
* `d078c8d` - L-03: Docs added
* `8ba9aeb` - L-03: Circle and square added
