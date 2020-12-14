from argparse import ArgumentParser

from datetime import datetime
from dateutil import tz

from scripts import runner, convert


def get_days():
    start = datetime(2020, 12, 1, tzinfo=tz.gettz('EST'))
    curr  = datetime.now(tz=tz.tzlocal())
    days  = (curr - start).days + 1
    return min(days, 25)


parser = ArgumentParser(prog='python .')
parser.add_argument('action', action='store', nargs='?', default='run',
                    choices=['run', 'make', 'tex'])
parser.add_argument('-d', '--day', action='store', nargs='?', type=int,
                    default=None)
parser.add_argument('-t', '--tex', action='store', nargs='?', default=None)
parser.add_argument('-f', '--file', action='store', nargs='?', default=None)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.day is not None and args.day not in range(1, 26):
        parser.error(f'argument -d/--day: invalid choice: {args.day} '
                     '(choose between 1 to 25 inclusive)')

    if args.action == 'run':
        if args.day is None:
            for i in range(1, get_days() + 1):
                runner.run_module(i, auto_new=True)
        else:
            runner.run_module(args.day)
    elif args.day is None:
        parser.error('argument -d/--day: Day must be required')
    elif args.action == 'make':
        print(f'Making boilerplate code for Day {args.day}... ', end='')
        runner.make_boilerplate(args.day)
        print('DONE!')
    elif args.tex is None:
        parser.error('argument tex: require tex input')
    elif args.action == 'tex':
        print('Creating file...')
        file = convert.make_tex_image(args.tex, args.day, args.file)
        print('DONE!')
