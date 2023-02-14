import mongoengine as me
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from settings import MONGODB_SETTINGS
from mods.models import Super_user


def set_password(user, password):
    user.update(password=generate_password_hash(password, method='sha256'))

def create_superuser(**kw):
    if kw.get('password') != kw.pop('retype_password'):
        return 'Passwords do not match!'
    if len(kw.get('password')) < 6:
        return 'Password must be at least 6 characters!'
    if Super_user.objects(username=kw.get('username')):
        return 'Username already exists!'
    if Super_user.objects(email=kw.get('email')):
        return 'Email already exists!'
    password = kw.pop('password')
    superuser = Super_user(**kw)
    superuser.save()
    superuser.set_password(password)

def main():
    print('Create a new super user')
    data = dict(
        username = input('Username: '),
        email = input('Email: '),
        fname = input('Firstname: '),
        lname = input('Lastname: '),
        password = input('Password: '),
        retype_password = input('Retype password: '),
    )
    err = create_superuser(**data)
    if err:
        print(err)
    else:
        print('Successfully created.')


if __name__ == '__main__':
    me.connect(**MONGODB_SETTINGS)
    attrs = Super_user._fields | dict(set_password=set_password)
    Super_user = type('Super_user', (me.Document, UserMixin), attrs)
    main()
