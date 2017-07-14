# Generate test Email

from random import randint
from subprocess import call

FILE = 'ignore-email.txt'
COMMAND = 'pbcopy < {file}'.format(file=FILE)
EMAIL = 'mkochubeevsky-{num}@j.mail'
MIN, MAX = 0, 10**4

def main():
    write_new()
    copy_current()

def copy_current():
    call(COMMAND, shell=True)

def write_new():
    num = randint(MIN, MAX)
    with open(FILE, 'w+') as f:
        next_email = EMAIL.format(num=num)
        f.write(next_email)

if __name__ == '__main__':
    main()
