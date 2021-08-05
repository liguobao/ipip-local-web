# manage.py

import sys

from flask.cli import FlaskGroup
import subprocess
import sys

from src import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def flake():
    """Runs flake8 on the project."""
    subprocess.run(['flake8', 'project'])


if __name__ == '__main__':
    cli()
