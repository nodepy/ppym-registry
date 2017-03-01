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
import sys

config = require('./lib/config')
models = require('./lib/models')
app = require('./lib/app')
require('./lib/views/api')
require('./lib/views/browse')
require('./lib/views/docs')


def main():
  if models.CURRENT_REVISION != models.TARGET_REVISION:
    print('error: database not upgraded. The current revision is {} but '
        'we expected revision {}'.format(models.CURRENT_REVISION,
          models.TARGET_REVISION))
    print('error: use \'ppy-registry migrate\' to upgrade the database')
    sys.exit(1)

  host = config['registry.host']
  port = int(os.getenv('', int(config['registry.port'])))
  debug = (config['registry.debug'].lower().strip() == 'true')
  if debug:
    # TODO: Support Werkzeug livereloader in ppy environments.
    #       See ppym/engine#6.
    print('note: Unfortunately, Flask debug mode (specifically livereload) '
        'is currently not supported in ppy environments.')
    debug = False

  app.run(host=host, port=port, debug=debug)


if require.main == module:
  main()