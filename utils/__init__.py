import os
from time import perf_counter


def run(*parts, pad=''):
    for i, part in enumerate(parts, start=1):
        start  = perf_counter()
        answer = part()
        end    = perf_counter()
        timed  = end - start
        print(f'{pad}Part {i}: {answer:<16} [{timed:0.6f}s]')


def get_data(dir):
    path = os.path.join(dir, 'input.txt')
    with open(path, 'r') as in_file:
        return in_file.read()


mapf = lambda f: lambda *args, **kwargs: f(map(*args, **kwargs))
map_sum  = mapf(sum   )
map_list = mapf(list  )
map_dict = mapf(dict  )
map_sort = mapf(sorted)
