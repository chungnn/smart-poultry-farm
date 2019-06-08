# -*- coding: utf-8 -*-
from flask_script import Manager
from app.app import create_app, configure_app
from app import DEFAULT_GLOBAL_CONFIG_FILE
import sys

# utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

# init Flask app
app = create_app()
manager = Manager(app)

# run AgentStats API using Flask-Script
@manager.option('-c', '--config', dest='config_file', default=DEFAULT_GLOBAL_CONFIG_FILE)
def runserver(config_file):
    """Run in local machine."""
    configure_app(app, filename=config_file)
    app.run(host='0.0.0.0', port=8125, use_reloader=False, )


# run AgentStats API using Gunicorn
def build_app(config_file=DEFAULT_GLOBAL_CONFIG_FILE):
    configure_app(app, filename=config_file)
    return app


if __name__ == "__main__":
    # manager.run(default_command='runserver')
    configure_app(app)
    app.run(host='0.0.0.0', port='8126')
