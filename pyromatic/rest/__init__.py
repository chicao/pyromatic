import os
import logging

logger = logging.getLogger(__name__)


def includeme(config):
    config.add_route('storagerooms', '/storagerooms', request_method='GET')