# -*- coding: utf-8 -*-
import os
import click
import pyramid.paster

from freezegun import freeze_time
from paste.deploy import loadapp
from waitress import serve

@click.group()
def cli():
    pass


@cli.command()
@click.option('-e', '--environment', envvar='ENVIRONMENT', default='development')
@click.option('-p', '--port', envvar='PORT', default=6544, type=int)
@click.option('-f', '--freeze_date', envvar='FREEZE_DATE', default=None)
def web(environment, port, freeze_date=None):
    if freeze_date:
        freezer = freeze_time(freeze_date)
        freezer.start()

    app = loadapp('config:%s.ini' % environment, relative_to='.')
    pyramid.paster.get_app('%s.ini#main' % environment)
    pyramid.paster.setup_logging('%s.ini#main' % environment)
    serve(app, host='0.0.0.0', port=port, url_scheme='http')

    if freeze_date:
        freezer.stop()


if __name__ == '__main__':
    cli()