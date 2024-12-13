import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

size_requirements = {'circle': {'perimeter': 1, 'area': 1}, 'square': {'perimeter': 1, 'area': 1}}


def calc(fig, func, size):
    '''
    Функция не возвращает значение, но выводит на экран строку, указывающую, что было вычислено для данной фигуры (площадь или периметр) и сам результат вычислений.

            Параметры:
                    fig (str)- название фигуры,
                    func (str)- название функции,
                    size (list)- размер
    '''

    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}. Available figures are: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}. Available functions are: {funcs}")

    required_size = size_requirements.get(fig, {}).get(func, 1)
    if len(size) != required_size:
        raise ValueError(f"Invalid number of size for {fig} and {func}. Expected {required_size}, got {len(size)}")

    if any(s <= 0 for s in size):
        raise ValueError(f"Invalid size: {size}. Sizes must be positive numbers.")

    result = eval(f'{fig}.{func}(*{size})')
    return f'{func} of {fig} is {result}'


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    result = calc(fig, func, size)
    print(result)


