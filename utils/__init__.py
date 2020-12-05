def get_data(path='./input.txt'):
    with open(path, 'r') as in_file:
        return in_file.read()

mapf = lambda f: lambda *args, **kwargs: f(map(*args, **kwargs))
map_sum  = mapf(sum   )
map_list = mapf(list  )
map_sort = mapf(sorted)