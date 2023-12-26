import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-v', "--verbose", help="increase output verbosity",
#                     action="store_true")
# parser.add_argument('-s', '--secret', help='secret to give')
# parser.add_argument('echo', help='echo something')
# args = parser.parse_args()


# if args.verbose:
#     print("verbosity turned on")

# print(args.echo)
# print(args.secret)

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
parser.add_argument('square', help='value to square and print to stdout', type=int)
parser.add_argument('-c', '--cube', help='to cube a passed value', type=int)
parser.add_argument('-stuff', help='print stuff', default='stuff')

args = parser.parse_args()

value = args.square ** 2
if args.verbose:
  print(f'The square of {args.square} is {str(value)}')
else:
  print(value)

if args.cube:
  print(f'cube of {args.cube} is {args.cube ** 3}')

print(args.stuff)