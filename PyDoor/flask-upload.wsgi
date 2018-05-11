activate_this = '/home/max/.virtualenvs/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/max/Projekte/flask-upload')

from server import app as application
