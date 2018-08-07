import collections

from pyromatic.shared.request_object import InvalidRequestObject, ValidRequestObject

class StorageRoomListRequestObject(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, data):
        invalid_req = InvalidRequestObject()
        if 'filters' in data and not isinstance(data['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return StorageRoomListRequestObject(filters=data.get('filters', None))


class StorageRoomCreateRequestObject(ValidRequestObject):
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_dict(cls, data):
        invalid_req = InvalidRequestObject()
        if 'filters' in data and not isinstance(data['filters'], collections.Mapping):
            invalid_req.add_error('data', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return StorageRoomCreateRequestObject(data=data.get('data', None))