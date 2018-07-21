import os
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    if 'SQLALCHEMY_URL' in os.environ:
        settings['sqlalchemy.url'] = os.environ['SQLALCHEMY_URL']

    elif 'POSTGRES_HOST' in os.environ:
        settings['sqlalchemy.url'] = 'postgres://{}:{}@{}:{}/{}'.format(
            os.environ['POSTGRES_USER'],
            os.environ['POSTGRES_PASSWORD'],
            os.environ['POSTGRES_HOST'],
            os.environ['POSTGRES_PORT'],
            os.environ['POSTGRES_DB'],
        )

    config = Configurator(settings=settings)
    config.include('.rest')
    config.scan()

    return config.make_wsgi_app()
