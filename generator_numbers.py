import re
from typing import Callable

def generator_numbers(text: str):
        numbers = re.findall(r'\b\d+\.\d+\b', text)
        yield from map(float, numbers)

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    return sum(numbers_generator)
    

text = "20.12 or 12.28 . 333.1  and 2.9  or 0.2 and 2 or4.4 end 5.5."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
