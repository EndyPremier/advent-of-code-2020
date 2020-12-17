import shutil
from os import mkdir

from utils import run


def make_boilerplate(day):
    shutil.copytree('day00', f'day{day:02}')
    shutil.move(f'day{day:02}/day00.py', f'day{day:02}/day{day:02}.py')
    open(f'day{day:02}/input.txt', 'a').close()
    mkdir(f'day{day:02}/img')


def run_module(day, auto_new=False):
    print(f'Day {day:02}')
    try:
        module_name = f'day{day:02}.day{day:02}'
        module = __import__(module_name, fromlist=('part_one', 'part_two'))
        run(module.part_one, module.part_two, pad='  ')
    except ModuleNotFoundError as e:
        print(' ', e)
        if auto_new:
            print('  Making new directory from boilerplate...', end='')
            make_boilerplate(day)
            print('DONE!')
        else:
            print(f'  Do you mean `python . make -d {day}`?')
    except Exception as e:
        print(' ', e)
