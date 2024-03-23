def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(cache) # Перевіряємо чи працює кешування у словнику
        return cache[n]
    return fibonacci

fib = caching_fibonacci()

print(fib(3))
print(fib(5))
print(fib(7))