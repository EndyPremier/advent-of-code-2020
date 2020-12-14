from argparse import ArgumentParser

from datetime import datetime
from dateutil import tz

from scripts.runner import run_module, make_boilerplate


def get_days():
    start = datetime(2020, 12, 1, tzinfo=tz.gettz('EST'))
    curr  = datetime.now(tz=tz.tzlocal())
    days  = (curr - start).days + 1
    return min(days, 25)


parser = ArgumentParser(prog='python .')
parser.add_argument('action',
                    action='store',
                    nargs='?',
                    choices=['run', 'make', 'tex'],
                    default='run')
parser.add_argument('-d', '--day',
                    action='store',
                    type=int,
                    default=None)

def raise_empty_days_error():
    parser.error(f'argument -d/--day: invalid choice: {args.day} '
                 '(choose between 1 to 25 inclusive)')


if __name__ == "__main__":
    args = parser.parse_args()
    if args.day is not None and args.day not in range(1, 26):
        raise_empty_days_error()

    if args.action == 'run':
        if args.day is None:
            for i in range(1, get_days() + 1):
                run_module(i)
        else:
            run_module(args.day)
    elif args.day is None:
        raise_empty_days_error()
    elif args.action == 'make':
        make_boilerplate(args.day)
    elif args.action == 'tex':
        pass
