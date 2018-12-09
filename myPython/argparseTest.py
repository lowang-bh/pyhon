#!/usr/bin/env python

import argparse


def default_parser(params=None):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('--length', default='10', type=int)
    parser.add_argument('--width', default=10.5, type=int)
    args = parser.parse_args(params)
    print("-----test default_parser------")
    print(args)
    return args


def test_pararent(params=None):
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--parent', type=int)
    foo_parser = argparse.ArgumentParser(parents=[parent_parser])
    foo_parser.add_argument('foo')
    if params is None:
        params = ['--parent', '2', 'XXX']
    args = foo_parser.parse_args(params)
    print("-----test pararent------")
    print(args)

    return args


def test_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs=2)
    parser.add_argument('bar', nargs=1)
    parser.parse_args('c --foo a b'.split())
    args = parser.parse_args()

    return args


def test_nargs(params=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs=2)
    parser.add_argument('bar', nargs=1)
    parser.add_argument('--default', nargs='+', default='default when nargs=+')
    parser.add_argument('--any', nargs='*', default='at least one')
    parser.add_argument(
            '--keep-by-hours',
            help='Will keep all tags that are newer than specified hours.',
            default=24,
            nargs='?',
            metavar='Hours')
    args = parser.parse_args(params)
    print("-------test nargs-----")
    # print(parser.print_help())
    print(args)
    if args.keep_by_hours:
        print("keep by hours: %s" % args.keep_by_hours)
    return args


def test_store_const(params=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs='?', const='const', default='d')
    parser.add_argument('--noconst', nargs='?', default='default to noconst')
    parser.add_argument('bar', nargs='?', default='d')
    parser.add_argument('constbar', nargs='?', const='constbar', default='d')

    print("-------test_store_const-------")
    print(parser.parse_args(['XX', '--foo', 'YY']))
    print(parser.parse_args(['XX', '--foo', '--noconst']))
    print(parser.parse_args([]))


def test_store_default():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', default='d')
    parser.add_argument('--noconst', default='default to noconst')
    parser.add_argument('bar', default='d')
    parser.add_argument('constbar', nargs='?', default='default without position')

    print("-------test_store_default-------")
    # print(parser.parse_args(['XX']))
    print(parser.parse_args(['XX', '--foo', 'foo']))
    # print(parser.parse_args([]))


def test_store(params=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true')
    parser.add_argument('--bar', action='store_false')
    parser.add_argument('--baz-bash', action='store_false', dest="bash")
    args = parser.parse_args(params)
    print("-----test store ture and false------")
    print(args, args.foo)
    return args


if __name__ == "__main__":
    args = default_parser(['7', '-1', '42', "--width", '10'])
    print(args.accumulate(args.integers))
    print(args.integers, args.accumulate, args.width)
    print(vars(args))
    test_pararent()
    test_store_const()
    test_store_default()
    test_nargs('c --foo  a b '.split())
    test_nargs('bar --foo  fooa foob --any'.split())

    test_store('--foo'.split())

    default_parser(["-h"])
