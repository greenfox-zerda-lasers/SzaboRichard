import sys

print(sys.argv)

if len(sys.argv) == 1:
    print('No args were given.')
elif sys.argv[1] == 'kutya':
    print('vau')
