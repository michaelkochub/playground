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

def get_email():
    num = randint(MIN, MAX)
    return EMAIL.format(num=num)

def write_new():
    with open(FILE, 'w+') as f:
        f.write(get_email())

if __name__ == '__main__':
    main()
