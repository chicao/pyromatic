import json

from pyromatic.serializers import storageroom_serializer as srs
from pyromatic.domain.storageroom import StorageRoom

def test_serialize_domain_storageroom():
    room = StorageRoom('f853578c-fc0f-4e65-81b8-566c5dffa35a',
                       size=200,
                       price=10,
                       longitude=-0.09998975,
                       latitude=51.75436293)

    expected_json = ('{'
                     '"code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",'
                     '"size": 200,'
                     '"price": 10,'
                     '"longitude": -0.09998975,'
                     '"latitude": 51.75436293'
                     '}'
    )

    assert json.loads(json.dumps(room, cls=srs.StorageRoomEncoder)) \
        == json.loads(expected_json)
