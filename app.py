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

import flask
import jinja2
import markdown

models = require('./models')
resources = require('./resources')


app = flask.Flask('ppy-registry')
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Initialize the Jinja environment globals and filters..
app.jinja_env.globals.update({
  'active': lambda v, x: jinja2.Markup('class="active"') if v == x else '',
  'User': models.User,
  'Package': models.Package,
  'PackageVersion': models.PackageVersion,
  'markdown_resource': lambda x: jinja2.Markup(resources.markdownify(x)),
})

app.jinja_env.filters.update({
  'markdown': lambda x: jinja2.Markup(resources.markdown(x))
})

exports = app
