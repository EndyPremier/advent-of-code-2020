def make_dict(passport):
    return dict(entry.split(':') for entry in passport.split())

def get_data(path='./input.txt'):
    with open(path, 'r') as in_file:
        return in_file.read()

DATA = [make_dict(passport) for passport in get_data().split('\n\n')]
