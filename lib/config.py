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

import os

config = require('ppym/lib/config')
config.defaults.update({
  'registry.host': 'localhost',
  'registry.port': '8000',
  'registry.visible.host': '${registry.host}:${registry.port}',
  'registry.visible.url_scheme': 'http',
  'registry.debug': 'false',
  'registry.prefix': './ppy_registry',
  'registry.mongodb.host': 'localhost',
  'registry.mongodb.port': '27017',
  'registry.mongodb.db': 'ppy_registry',
  'registry.mongodb.username': None,
  'registry.mongodb.password': None,
  'registry.email.origin': 'no-reply@${registry.visible.host}',
  'registry.email.smtp_host': 'localhost:25',
  'registry.email.smtp_ssl': 'false',
  'registry.email.require_verification': 'false',
  'registry.enforce_user_namespaces': 'true',
  'registry.accept_registrations': 'true'
})

config['registry.prefix'] = os.path.expanduser(config['registry.prefix'])
exports = config