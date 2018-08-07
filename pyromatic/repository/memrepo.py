from pyromatic.domain import storageroom as sr
from pyromatic.repository.validators import storageroom_validator as val


class MemRepo:
    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} not supported'.format(operator))

        operator = '__{}__'.format(operator)

        if key in ['size', 'price']:
            return getattr(element[key], operator)(int(value))

        elif key in ['latitude', 'longitude']:
            return getattr(element[key], operator)(float(value))

        return getattr(element[key], operator)(value)

    def list(self, filters=None):
        if not filters:
            return self._entries

        result = []
        result.extend(self._entries)

        for key, value in filters.items():
            result = [e for e in result if self._check(e, key, value)]

        return [sr.StorageRoom.from_dict(r) for r in result]


    def create(self, data=None):
        if not data:
            return self._entries

        storage_room_dict = val.validate(data) # responsavel por validar objs
        return sr.StorageRoom.from_dict(storage_room_dict)
