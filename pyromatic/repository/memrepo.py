from pyromatic.domain import storageroom as sr
#from pyromatic.repository.validators import storageroom_validator as val


class MemRepo:
    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check_filter(self, element, key, value):
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
            result = [e for e in result if self._check_filter(e, key, value)]

        return [sr.StorageRoom.from_dict(r) for r in result]


    def create(self, data=None):

        if not data:
            raise ValueError('No data was given for room creation')

        storage_room_keys = {'code',
                             'size',
                             'price',
                             'longitude', 
                             'latitude'}

        data_keys = {key for key in data.keys()}
        if data_keys != storage_room_keys:
            invalid = [k for k in data_keys if k not in storage_room_keys]
            raise ValueError('Keys {} are invalid'.format(', '.join(invalid)))

        room = sr.StorageRoom.from_dict(data)
        self._entries.append(room)

        return room