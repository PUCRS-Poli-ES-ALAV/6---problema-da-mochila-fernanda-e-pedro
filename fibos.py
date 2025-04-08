import time
import sys

# Set a new recursion limit (e.g., 10,000)
sys.setrecursionlimit(100000)


def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_iter(n):
    if n <= 1:
        return n
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def memoized_fibo(n):
    f = [-1] * (n + 1)
    return lookup_fibo(f, n)

def lookup_fibo(f, n):
    if f[n] >= 0:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f, n - 1) + lookup_fibo(f, n - 2)
    return f[n]


class Counter:
    def __init__(self):
        self.calls = 0
        self.instructions = 0

def fibo_rec_counted(n, counter):
    counter.calls += 1
    counter.instructions += 1
    if n <= 1:
        return n
    counter.instructions += 2  
    a = fibo_rec_counted(n - 1, counter)
    b = fibo_rec_counted(n - 2, counter)
    counter.instructions += 1  
    return a + b

def fibo_iter_counted(n, counter):
    counter.calls += 1
    counter.instructions += 3  
    if n <= 1:
        return n
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        counter.instructions += 3  
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def memoized_fibo_counted(n, counter):
    counter.calls += 1
    f = [-1] * (n + 1)
    for i in range(n + 1):
        counter.instructions += 1  
        f[i] = -1
    return lookup_fibo_counted(f, n, counter)

def lookup_fibo_counted(f, n, counter):
    counter.calls += 1
    counter.instructions += 1
    if f[n] >= 0:
        return f[n]
    counter.instructions += 1
    if n <= 1:
        f[n] = n
    else:
        counter.instructions += 2  
        f[n] = lookup_fibo_counted(f, n - 1, counter) + lookup_fibo_counted(f, n - 2, counter)
    counter.instructions += 1  
    return f[n]


test_values_basic = [4, 8, 16, 32]
test_values_extended = [128, 1000, 10000]
results = {}


for algo_name, func in [
    ("FIBO-REC", fibo_rec_counted),
    ("FIBO", fibo_iter_counted),
    ("MEMOIZED-FIBO", memoized_fibo_counted)
]:
    results[algo_name] = {}
    test_values = test_values_basic if algo_name == "FIBO-REC" else test_values_basic + test_values_extended
    for n in test_values:
        counter = Counter()
        start = time.time()
        result = func(n, counter)
        elapsed = time.time() - start
        results[algo_name][n] = {
            "value": result,
            "calls": counter.calls,
            "instructions": counter.instructions,
            "time_sec": elapsed
        }

print(results)
