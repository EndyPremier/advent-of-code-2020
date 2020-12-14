from string import ascii_letters, digits
from sympy import preview

from scripts import runner


ALPHANUM = set(ascii_letters + digits)
def gen_filename(s):
    return ''.join(c for c in s if c in ALPHANUM) + '.png'


def make_tex_image(tex, day, file=None):
    if file is None:
        file = gen_filename(tex)
    filename = f'problems/day{day:02}/img/{file}'
    try:
        preview(tex, viewer='file', filename=filename, euler=False)
        return filename
    except FileNotFoundError:
        print(f"day{day:02} doesn't exist, create new boilerplate... ", end='')
        runner.make_boilerplate(day)
        print('DONE! Trying again...')
        make_tex_image(tex, day, file)
