from datetime import datetime
from dateutil import tz
import shutil


def _make_boilerplate(day):
    shutil.copytree('day00', f'day{day:02}')
    shutil.move(f'day{day:02}/day00.py', f'day{day:02}/day{day:02}.py')
    open(f'day{day:02}/input.txt', 'a').close()


REQUIRED_METHODS = ('part_one', 'part_two')
def _import_module(day):
    module_name = f'day{day:02}.day{day:02}'
    return __import__(module_name, fromlist=REQUIRED_METHODS)

def _run_module(day):
    print(f'Day {day:02}')
    try:
        module = _import_module(day)
        print('  Part 1:', module.part_one())
        print('  Part 2:', module.part_two())
    except ModuleNotFoundError as e:
        print(' ', e)
        print('  Making new directory from boilerplate...', end='')
        _make_boilerplate(day)
        print('DONE!')
    except Exception as e:
        print(' ', e)


def _get_days():
    start = datetime(2020,12,1, tzinfo=tz.gettz('EST'))
    curr  = datetime.now(tz=tz.tzlocal())
    days  = (curr - start).days + 1
    return min(days, 25)


if __name__ == "__main__":
    for i in range(1, _get_days() + 1):
        _run_module(i)
