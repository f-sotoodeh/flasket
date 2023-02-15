from getpass import getpass

import mongoengine as me

from settings import MONGODB_SETTINGS
from mods import models


def create_superuser(**kw):
    if kw.get('password') != kw.pop('retype_password'):
        return 'Passwords do not match!'
    if len(kw.get('password')) < 6:
        return 'Password must be at least 6 characters!'
    if SuperUser.objects(username=kw.get('username')):
        return 'Username already exists!'
    if SuperUser.objects(email=kw.get('email')):
        return 'Email already exists!'
    kw['password'] = models.Super_user.hash_password(kw.pop('password'))
    SuperUser(**kw).save()

def main():
    print('Create a new super user')
    data = dict(
        username = input('Username: '),
        email = input('Email: '),
        fname = input('Firstname: '),
        lname = input('Lastname: '),
        password = getpass('Password: '),
        retype_password = getpass('Retype password: '),
    )
    err = create_superuser(**data)
    if err:
        print(err)
    else:
        print('Successfully created.')


if __name__ == '__main__':
    me.connect(**MONGODB_SETTINGS)
    SuperUser = type('SuperUser', (me.Document,), models.Super_user._fields)
    main()
