from pyromatic.shared.domain_model import DomainModel


class StorageRoom(object):

    def __init__(self, code, size, price, latitude, longitude):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_dict(cls, data):
        room = StorageRoom(
            code=data['code'],
            size=data['size'],
            price=data['price'],
            latitude=data['latitude'],
            longitude=data['longitude'],
        )

        return room

# ????
DomainModel.register(StorageRoom)
