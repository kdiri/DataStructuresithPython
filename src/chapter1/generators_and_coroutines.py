# compares the running time of a list compared to a generator
import time
from typing import Generator, List

# generator function creates an iterator of odd numbers between n and m


def odd_gen(n: int, m: int) -> Generator:
    while n < m:
        yield n
        n += 2


# builds a list of odd numbers between n and m
def odd_lst(n: int, m: int) -> List:
    lst: list = []
    while n < m:
        lst.append(n)
        n += 2
    return lst


# the time it takes to perform sum on an iterator
t1 = time.time()
sum(odd_gen(1, 1000000))
print(f"Time to sum an iterator: {time.time() - t1}")
# the time it takes to build and sum a list
t1 = time.time()
sum(odd_lst(1, 1000000))
print(f"Time to build and sum a list: {time.time() - t1}")
