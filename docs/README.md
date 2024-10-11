# Functions and descriptions
## `calculate.py`
### `def calc(fig, func, size):`
- Calculates the value of the specified function for the specified shape based on its dinensions.
- Exapmple of a call:
```python
>> calc('circle', 'area', 7)
153.93804
```
## `circle.py`
### `def area(r):`
- Calculates the area of a circle by a given radius.
- Exapmple of a call:
```python
>> area(7)
153.93804
```

### `def perimetr(r):`
- Calculates the length of a circle by a given radius.
- Exapmple of a call:
```python
>> perimetr(7)
43.9823
```

## `square.py`
### `def area(a):`
- Calculates the area of a square along a given side length.
- Exapmple of a call:
```python
>> area(7)
49.0
```

### `def perimetr(a):`
- Calculates the perimetr of a square along a given side length.
- Exapmple of a call:
```python
>> perimetr(7)
28.0
```

## `triangle.py`
### `def area(a, b, c):`
- Calculates the half-meter of a triangle by the specified side lengths.
- Exapmple of a call:
```python
>> area(3, 4, 5)
6.0
```

### `def perimetr(a, b, c):`
- Calculates the perimetr of a triangle by the specified side lengths.
- Exapmple of a call:
```python
>> perimetr(3, 4 ,5)
12.0
```

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

