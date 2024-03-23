import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\b', text)
    yield from map(float, numbers)

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    return sum(numbers_generator)
    

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
