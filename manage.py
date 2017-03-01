# Copyright (c) 2017 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import click
import os

models = require('./lib/models')


@click.group()
def main(): pass


@main.command()
def drop():
  reply = input('Do you really want to drop all data in the database? ')
  if reply  in ('y', 'yes'):
    print('Okay..')
    models.User.drop_collection()
    models.Package.drop_collection()
    models.PackageVersion.drop_collection()
  else:
    print('Better so.')


@main.command()
@click.option('-u', '--username')
@click.option('-p', '--password')
@click.option('-e', '--email')
@click.option('--superuser', is_flag=True)
@click.option('--verified', is_flag=True)
def adduser(username, password, email, superuser, verified):
  if not username:
    username = input('Username? ')
  if models.User.objects(name=username).first():
    print('User {} already exists'.format(username))
    return 1

  if not password:
    password = input('Password? ')
    if input('Confirm Password? ') != password:
      print('passwords do not match')

  if not email:
    email = input('Email? ')
  if models.User.objects(email=email).first():
    print('Email {} already in use'.format(email))
    return 1

  user = models.User(username, models.hash_password(password), email,
      superuser=superuser, validated=verified)
  user.save()
  print('User created.')


@main.command()
@click.option('-d', '--dry', is_flag=True)
def migrate(dry):
  """
  Use after an update to upgrade the database.
  """

  migrate = require('./lib/migrate').Migration(models.db,
      models.CURRENT_REVISION, models.TARGET_REVISION,
      os.path.join(__directory__, 'migrations'), dry=dry)
  migrate.execute()
  if not dry:
    models.MigrationRevision.set(models.TARGET_REVISION)


if require.main == module:
  main()