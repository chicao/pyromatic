import json


class StorageRoomEncoder(json.JSONEncoder):

    def default(self, obj):
        try:
            to_serialize = {
                'code': obj.code,
                'size': obj.size,
                'price': obj.price,
                'latitude': obj.latitude,
                'longitude': obj.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(obj)